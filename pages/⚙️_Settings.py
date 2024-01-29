import streamlit as st

if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ""

st.set_page_config(page_title="🤖Multi_Agents_Group Settings", layout="wide")

st.title("🤖Multi_Agents_Group Settings")

model = st.selectbox('Model', ["gpt-4-32k","gpt-3.5-turbo"])

openai_api_key = st.text_input("API Key", value=st.session_state["OPENAI_API_KEY"], max_chars=None, key=None, type='password')

saved = st.button("Save")

if saved:
    st.session_state["Model"]=model 
    st.session_state["OPENAI_API_KEY"] = openai_api_key