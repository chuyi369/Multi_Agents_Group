import autogen
import streamlit as st
import time
import threading
import random
import os
from queue import Queue
from typing import Any,Dict,List,Optional, Union
from streamlit_extras.let_it_rain import rain
from typing_extensions import Annotated
from autogen import AssistantAgent,UserProxyAgent,Agent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
import chromadb



class Print_Message(Agent):
    def __init__(self, agent):
        self.agent=agent
    def _print_received_message(self,message:Union[Dict,str],sender: Agent):
        print("Type of message:", type(message))
        all_msg=[]
        def st_write(msg):
            st.write(msg)
            all_msg.append(msg)
        with st.chat_message(sender.name,avatar=avatars[sender.name]):
            s=sender.name+"(to"+self.agent.name+"):\n"
            st_write(s)
            if isinstance(message, str):
                st_write(message)
            else:
                st_write(message['content'])
            history.append({'role':sender.name,'content':all_msg[1]})
            
            



class AgentGroupChatManager(autogen.GroupChatManager):
    def _print_received_message(self,message:Union[Dict,str],sender: Agent):
        Print_Message(self)._print_received_message(message,sender)
        super()._print_received_message(message,sender)

class AgentGroupAssistant(AssistantAgent):
    def _print_received_message(self,message:Union[Dict,str],sender: Agent):
        Print_Message(self)._print_received_message(message,sender)
        super()._print_received_message(message,sender)

class AgentGroupUser(UserProxyAgent):
    def _print_received_message(self,message:Union[Dict,str],sender: Agent):
        Print_Message(self)._print_received_message(message,sender)
        super()._print_received_message(message,sender)

    
class AgentGroupRetrieveUser(RetrieveUserProxyAgent):
    def _print_received_message(self,message:Union[Dict,str],sender: Agent):
        Print_Message(self)._print_received_message(message,sender)
        super()._print_received_message(message,sender)

def reset_agent():
    boss.reset()
    boss_assistant.reset()
    engineer.reset()
    scientist.reset()
    product_manager.reset()
    engineer_assistant.reset()
    plan_examer.reset()



@st.cache_resource
def initHistory():
    history=[]
    return history

@st.cache_resource
def initalAgents():
    print('initalAgents...')
    assistant=AgentGroupAssistant(
        name="assistant",
        llm_config={
            "seed":42,
            "config_list":config_list,
            "temperature":0
        },
    )
    user_proxy = AgentGroupUser(
            name="user",
            human_input_mode="ALWAYS",
            max_consecutive_auto_reply=10,
            code_execution_config={"work_dir": "coding", "use_docker": False},
            is_termination_msg=lambda x: x.get(
                "content", "").rstrip().endswith("TERMINATE"),
        )
    termination_msg=lambda x: isinstance(x,dict) and "TERMINATE"==str(x.get("content", ""))[-9:].upper()

    boss=AgentGroupUser(
        name="Boss",
        system_message="The boss who ask questions and give tasks, Interact with the product_manager to discuss the plan.",  
        code_execution_config=False,   
    )
    
    boss_assistant=AgentGroupRetrieveUser(
        name="Boss_Assistant",
        is_termination_msg=termination_msg, 
        human_input_mode="NEVER",
        system_message="Assistant who has extra content retrieval power for solving difficult problems",
        max_consecutive_auto_reply=3,
        code_execution_config=False,
        retrieve_config={
            "docs_path":"./save/news_report.md",
            "chunk_token_size":1000,
            "model":config_list[0]["model"],
            "client":chromadb.PersistentClient(path="./chromadb"),
            "collection_name":"groupchat",
            "get_or_create":True,       
              },
    )
    engineer=AgentGroupAssistant(
        name="Engineer",
        system_message='''You are a engineer.You follow an approved plan.You write python/shell code to solve tasks.
        Wrap the code in a code block that specifies the script type. Do not ask others to copy and paste the result. 
        check the execution result returned by the Engineer_Assistant.If the result indicates there is an eror, fix the eror and autput the code again.
        suggest the full code instead of partial code or code changes. ''',
        llm_config=llm_config,
    )
    product_manager=AgentGroupAssistant(
        name="Product_Manager",
        is_termination_msg=termination_msg,        
        system_message='''Product_Manager.Suggest a plan. Revise the plan based on feedback from admin and critic, until Boss approval.
        The plan may involve an engineer who can write code and a scientist who doesn't write code.
        Explain the plan first. Be clear which step is performed by an engineer, and which step is performed by a scientist.''',
        llm_config=llm_config,
    )
    plan_examer=AgentGroupAssistant(
        name="Plan_Examer",
        system_message="Plan_Examer.You second turn,check the plan by product_manager:If engineer,scientist,engineer_assistant,boss has their steps or role in this task and then feedback",
        llm_config=llm_config,
    )
    scientist=AgentGroupAssistant(
        name="Scientist",
        system_message='''Scientist.You follow an approved plan.You are able to categorize
        papers after seeing their abstracts printed,You don't write code''',
        llm_config=llm_config,
    )    
    engineer_assistant=AgentGroupUser(
        name="Engineer_Assistant",
        code_execution_config={"work_dir": "groupchat","last_n_messages":3, "use_docker": False},
        human_input_mode="NEVER",
        system_message="Excute/Run the code written by the engineer and check if the result is proper(if the result is empty or wrong give feed back to engineer),then report the result,If the result is too long(more than 1000 tokens),Please sumary ",
        llm_config=llm_config,
    )   
    boss.reset()
    boss_assistant.reset()
    engineer.reset()
    scientist.reset()
    product_manager.reset()
    engineer_assistant.reset()
    plan_examer.reset()
    groupchat=autogen.GroupChat(
        agents=[boss,engineer,scientist,product_manager,engineer_assistant,plan_examer],messages=[],max_round=12
    )
    manager=AgentGroupChatManager(groupchat=groupchat,llm_config=llm_config)
    return boss,boss_assistant,engineer,scientist,plan_examer,product_manager,engineer_assistant,manager



def norag_chat(PROBLEM):
    reset_agent()
    groupchat=autogen.GroupChat(
        agents=[boss,engineer,scientist,product_manager,engineer_assistant,plan_examer],messages=[],max_round=20
    )
    manager=AgentGroupChatManager(groupchat=groupchat,llm_config=llm_config)
    boss.initiate_chat(
        manager,
        message=PROBLEM,
        clear_history=False
    )    

def rag_chat(PROBLEM):
    reset_agent()
    def retrieve_content(message,n_results=3):
        boss_assistant.n_results=n_results
        update_context_case1,update_context_case2=boss_assistant._check_update_context(message)
        if (update_context_case1 or update_context_case2) and boss_assistant.update_context:
            boss_assistant.problem=message if not hasattr(boss_assistant,"problem") else boss_assistant.problem
            _,ret_msg=boss_assistant._generate_retrieve_user_reply(message)
        else:
            ret_msg=boss_assistant.generate_init_message(message,n_results=n_results)
        return ret_msg if ret_msg else message
    
    boss_assistant.human_input_mode="TERMINATE"

    llm_config= {
    "functions": [
        {
            "name": "retrieve_content",
            "description": "retrieve content for code generation and question answering.",
            "parameters": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "Refined message which keeps the original meaning and can be used retrieve content for code generation and question answering."
                    }
                },
                "required": ["message"]
            }
        }
    ],
    "config_list": config_list, 
    "timeout": 60,
    "seed": 42
}
    for agent in [engineer, product_manager, engineer_assistant]:
        agent.llm_config.update(llm_config)

    for agent in [boss, engineer, product_manager,engineer_assistant]:
        agent.register_function(
            function_map={
                "retrieve_content":retrieve_content,
            }
        )
    groupchat=autogen.GroupChat(
        agents=[boss,engineer,product_manager,engineer_assistant],messages=[],max_round=12,allow_repeat_speaker=False,
    )
    manager_llm_config = llm_config.copy()
    manager_llm_config.pop("functions")
    manager=AgentGroupChatManager(groupchat=groupchat,llm_config=manager_llm_config)

    boss.initiate_chat(
        manager,
        message=PROBLEM,
        clear_history=False
    )


os.environ["http_proxy"] = "http://localhost:7890"
os.environ["https_proxy"] = "http://localhost:7890"

os.environ['AUTOGEN_USE_DOCKER']='False'

avatars={"Chat_Manager":"🧑‍💼","Boss":"👨🏻‍💼","Boss_Assistant":"🧛‍♂️","Engineer":"👨‍💻","Scientist":"🧑‍💼","Product_Manager":"🤵🏻","Engineer_Assistant":"🕵🏻","Plan_Examer":"🧛‍♂️"}

config_list = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    file_location=".",
    filter_dict={
        "model": ["gpt-4-32k","gpt-3.5-turbo"],
    },
)


llm_config ={
    "timeout": 60,
    "seed": 42,
    "config_list": config_list,
    "temperature": 0,
     "max_tokens": 1024,
    
}


history=initHistory()
if 'input_msg' not in st.session_state:
    st.session_state.input_msg=None


if 'count' not in st.session_state:
    st.session_state.count=0

method = st.selectbox('Choose a method:', ['norag_chat','rag_chat'])

boss,boss_assistant,engineer,scientist,plan_examer,product_manager,engineer_assistant,manager=initalAgents()

@boss.register_for_execution()
@product_manager.register_for_llm()
@engineer_assistant.register_for_llm(description="terminate the group chat")
def terminate_group_chat(message: Annotated[str, "Message to be sent to the group chat."]) -> str:
    return f"[GROUPCHAT_TERMINATE] {message}"


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # 构建文件的保存路径
    save_path = os.path.join('./save', uploaded_file.name)
    # 将文件内容写入到保存路径
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

user_input=st.chat_input("Enter Input")


input_user_name="Chat_Manager"
if  'count' in st.session_state and st.session_state.count==0:
    if user_input is None:
        with st.chat_message(input_user_name,avatar=avatars[input_user_name]):
            st.write("chat manager:")
            st.write("有什么能为您效劳")
            st.write("eg: find papers on LLM agents from arxiv in the last week (no more than 30 papers), create amarkdown table of different domains.")    
    else:
        print('*******************************')
        st.session_state.count+=1
        if method == 'rag_chat':
            print("rag_chat!")
            rag_chat(user_input)
        elif method == 'norag_chat':
            print("norag_chat!")
            norag_chat(user_input)
else:
    if user_input is None:
        for his in history:
            curMsg=his
            with st.chat_message(his['role'],avatar=avatars[his['role']]):
                st.write(curMsg['role']+'(tochat_manager):\n')
                st.markdown(curMsg['content'])       
        with st.chat_message(input_user_name,avatar=avatars[input_user_name]):
            st.write("chat manager:")
            st.write("请提出您的问题")
    else:
        for his in history:
            curMsg=his
            with st.chat_message(his['role'],avatar=avatars[his['role']]):
                st.write(curMsg['role']+'(tochat_manager):\n')
                st.markdown(curMsg['content'])
        if method == 'rag_chat':
            print("rag_chat!")
            rag_chat(user_input)
        elif method == 'norag_chat':
            print("norag_chat!")
            norag_chat(user_input)


