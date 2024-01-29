| Title | Authors | Abstract | Domain |
|-------|---------|----------|--------|
| From GPT-4 to Gemini and Beyond: Assessing the Landscape of MLLMs on Generalizability, Trustworthiness and Causality through Four Modalities | Authors:
Chaochao Lu, 
      
      Chen Qian, 
      
      Guodong Zheng, 
      
      Hongxing Fan, 
      
      Hongzhi Gao, 
      
      Jie Zhang, 
      
      Jing Shao, 
      
      Jingyi Deng, 
      
      Jinlan Fu, 
      
      Kexin Huang, 
      
      Kunchang Li, 
      
      Lijun Li, 
      
      Limin Wang, 
      
      Lu Sheng, 
      
      Meiqi Chen, 
      
      Ming Zhang, 
      
      Qibing Ren, 
      
      Sirui Chen, 
      
      Tao Gui, 
      
      Wanli Ouyang, 
      
      Yali Wang, 
      
      Yan Teng, 
      
      Yaru Wang, 
      
      Yi Wang, 
      
      Yinan He
      , et al. (11 additional authors not shown) | Multi-modal Large Language Models (MLLMs) have shown impressive abilities in generating reasonable responses with respect to multi-modal contents. However, there is still a wide gap between the performance of recent MLLM-based applications and the expectation of the broad public, even though the most powerful OpenAI's GPT-4 and Google's Gemini have been deployed. This paper strives to enhance understanding of the gap through the lens of a qualitative study on the generalizability, trustworthiness, and causal reasoning capabilities of recent proprietary and open-source MLLMs across four modalities: ie, text, code, image, and video, ultimately aiming to improve the transparency of MLLMs. We believe these properties are several representative factors that define the reliability of MLLMs, in supporting various downstream applications. To be specific, we evaluate the closed-source GPT-4 and Gemini and 6 open-source LLMs and MLLMs. Overall we evaluate 230 manually designed cases, where the qualitative results are then summarized into 12 scores (ie, 4 modalities times 3 properties). In total, we uncover 14 empirical findings that are useful to understand the capabilities and limitations of both proprietary and open-source MLLMs, towards more reliable downstream multi-modal applications.
        △ Less | Unknown |
| Under the Surface: Tracking the Artifactuality of LLM-Generated Data | Authors:
Debarati Das, 
      
      Karin De Langis, 
      
      Anna Martin, 
      
      Jaehyung Kim, 
      
      Minhwa Lee, 
      
      Zae Myung Kim, 
      
      Shirley Hayati, 
      
      Risako Owan, 
      
      Bin Hu, 
      
      Ritik Parkar, 
      
      Ryan Koo, 
      
      Jonginn Park, 
      
      Aahan Tyagi, 
      
      Libby Ferland, 
      
      Sanjali Roy, 
      
      Vincent Liu, 
      
      Dongyeop Kang | This work delves into the expanding role of large language models (LLMs) in generating artificial data. LLMs are increasingly employed to create a variety of outputs, including annotations, preferences, instruction prompts, simulated dialogues, and free text. As these forms of LLM-generated data often intersect in their application, they exert mutual influence on each other and raise significant concerns about the quality and diversity of the artificial data incorporated into training cycles, leading to an artificial data ecosystem. To the best of our knowledge, this is the first study to aggregate various types of LLM-generated text data, from more tightly constrained data like "task labels" to more lightly constrained "free-form text". We then stress test the quality and implications of LLM-generated artificial data, comparing it with human data across various existing benchmarks. Despite artificial data's capability to match human performance, this paper reveals significant hidden disparities, especially in complex tasks where LLMs often miss the nuanced understanding of intrinsic human-generated content. This study critically examines diverse LLM-generated data and emphasizes the need for ethical practices in data creation and when using LLMs. It highlights the LLMs' shortcomings in replicating human traits and behaviors, underscoring the importance of addressing biases and artifacts produced in LLM-generated content for future research and development. All data and code are available on our project page.
        △ Less | Unknown |
| Scientific Large Language Models: A Survey on Biological & Chemical Domains | Authors:
Qiang Zhang, 
      
      Keyang Ding, 
      
      Tianwen Lyv, 
      
      Xinda Wang, 
      
      Qingyu Yin, 
      
      Yiwen Zhang, 
      
      Jing Yu, 
      
      Yuhao Wang, 
      
      Xiaotong Li, 
      
      Zhuoyi Xiang, 
      
      Xiang Zhuang, 
      
      Zeyuan Wang, 
      
      Ming Qin, 
      
      Mengyao Zhang, 
      
      Jinlu Zhang, 
      
      Jiyu Cui, 
      
      Renjun Xu, 
      
      Hongyang Chen, 
      
      Xiaohui Fan, 
      
      Huabin Xing, 
      
      Huajun Chen | Large Language Models (LLMs) have emerged as a transformative power in enhancing natural language comprehension, representing a significant stride toward artificial general intelligence. The application of LLMs extends beyond conventional linguistic boundaries, encompassing specialized linguistic systems developed within various scientific disciplines. This growing interest has led to the advent of scientific LLMs, a novel subclass specifically engineered for facilitating scientific discovery. As a burgeoning area in the community of AI for Science, scientific LLMs warrant comprehensive exploration. However, a systematic and up-to-date survey introducing them is currently lacking. In this paper, we endeavor to methodically delineate the concept of "scientific language", whilst providing a thorough review of the latest advancements in scientific LLMs. Given the expansive realm of scientific disciplines, our analysis adopts a focused lens, concentrating on the biological and chemical domains. This includes an in-depth examination of LLMs for textual knowledge, small molecules, macromolecular proteins, genomic sequences, and their combinations, analyzing them in terms of model architectures, capabilities, datasets, and evaluation. Finally, we critically examine the prevailing challenges and point out promising research directions along with the advances of LLMs. By offering a comprehensive overview of technical developments in this field, this survey aspires to be an invaluable resource for researchers navigating the intricate landscape of scientific LLMs.
        △ Less | Unknown |
| K-QA: A Real-World Medical Q&A Benchmark | Authors:
Itay Manes, 
      
      Naama Ronn, 
      
      David Cohen, 
      
      Ran Ilan Ber, 
      
      Zehavi Horowitz-Kugler, 
      
      Gabriel Stanovsky | Ensuring the accuracy of responses provided by large language models (LLMs) is crucial, particularly in clinical settings where incorrect information may directly impact patient health. To address this challenge, we construct K-QA, a dataset containing 1,212 patient questions originating from real-world conversations held on K Health (an AI-driven clinical platform). We employ a panel of in-house physicians to answer and manually decompose a subset of K-QA into self-contained statements. Additionally, we formulate two NLI-based evaluation metrics approximating recall and precision: (1) comprehensiveness, measuring the percentage of essential clinical information in the generated answer and (2) hallucination rate, measuring the number of statements from the physician-curated response contradicted by the LLM answer. Finally, we use K-QA along with these metrics to evaluate several state-of-the-art models, as well as the effect of in-context learning and medically-oriented augmented retrieval schemes developed by the authors. Our findings indicate that in-context learning improves the comprehensiveness of the models, and augmented retrieval is effective in reducing hallucinations. We make K-QA available to to the community to spur research into medically accurate NLP applications.
        △ Less | Unknown |
| LongHealth: A Question Answering Benchmark with Long Clinical Documents | Authors:
Lisa Adams, 
      
      Felix Busch, 
      
      Tianyu Han, 
      
      Jean-Baptiste Excoffier, 
      
      Matthieu Ortala, 
      
      Alexander Löser, 
      
      Hugo JWL. Aerts, 
      
      Jakob Nikolas Kather, 
      
      Daniel Truhn, 
      
      Keno Bressem | Background: Recent advancements in large language models (LLMs) offer potential benefits in healthcare, particularly in processing extensive patient records. However, existing benchmarks do not fully assess LLMs' capability in handling real-world, lengthy clinical data.
  Methods: We present the LongHealth benchmark, comprising 20 detailed fictional patient cases across various diseases, with each case containing 5,090 to 6,754 words. The benchmark challenges LLMs with 400 multiple-choice questions in three categories: information extraction, negation, and sorting, challenging LLMs to extract and interpret information from large clinical documents.
  Results: We evaluated nine open-source LLMs with a minimum of 16,000 tokens and also included OpenAI's proprietary and cost-efficient GPT-3.5 Turbo for comparison. The highest accuracy was observed for Mixtral-8x7B-Instruct-v0.1, particularly in tasks focused on information retrieval from single and multiple patient documents. However, all models struggled significantly in tasks requiring the identification of missing information, highlighting a critical area for improvement in clinical data interpretation.
  Conclusion: While LLMs show considerable potential for processing long clinical documents, their current accuracy levels are insufficient for reliable clinical use, especially in scenarios requiring the identification of missing information. The LongHealth benchmark provides a more realistic assessment of LLMs in a healthcare setting and highlights the need for further model refinement for safe and effective clinical application.
  We make the benchmark and evaluation code publicly available.
        △ Less | Unknown |
| Wordflow: Social Prompt Engineering for Large Language Models | Authors:
Zijie J. Wang, 
      
      Aishwarya Chakravarthy, 
      
      David Munechika, 
      
      Duen Horng Chau | Large language models (LLMs) require well-crafted prompts for effective use. Prompt engineering, the process of designing prompts, is challenging, particularly for non-experts who are less familiar with AI technologies. While researchers have proposed techniques and tools to assist LLM users in prompt design, these works primarily target AI application developers rather than non-experts. To address this research gap, we propose social prompt engineering, a novel paradigm that leverages social computing techniques to facilitate collaborative prompt design. To investigate social prompt engineering, we introduce Wordflow, an open-source and social text editor that enables everyday users to easily create, run, share, and discover LLM prompts. Additionally, by leveraging modern web technologies, Wordflow allows users to run LLMs locally and privately in their browsers. Two usage scenarios highlight how social prompt engineering and our tool can enhance laypeople's interaction with LLMs. Wordflow is publicly accessible at https://poloclub.github.io/wordflow.
        △ Less | Unknown |
| RomanSetu: Efficiently unlocking multilingual capabilities of Large Language Models models via Romanization | Authors:
Jaavid Aktar Husain, 
      
      Raj Dabre, 
      
      Aswanth Kumar, 
      
      Ratish Puduppully, 
      
      Anoop Kunchukuttan | This study addresses the challenge of extending Large Language Models (LLMs) to non-English languages, specifically those using non-Latin scripts. We propose an innovative approach that utilizes the romanized form of text as an interface for LLMs, hypothesizing that its frequent informal use and shared tokens with English enhance cross-lingual alignment. Focusing on Hindi, we demonstrate through Hindi-to-English translation and sentiment analysis tasks that romanized text not only significantly improves inference efficiency due to its lower fertility compared to native text but also achieves competitive performance with limited pre-training. Additionally, our novel multi-script prompting approach, which combines romanized and native texts, shows promise in further enhancing task performance. These findings suggest the potential of romanization in bridging the language gap for LLM applications, with future work aimed at expanding this approach to more languages and tasks.
        △ Less | Unknown |
| How Can Large Language Models Understand Spatial-Temporal Data? | Authors:
Lei Liu, 
      
      Shuo Yu, 
      
      Runze Wang, 
      
      Zhenxun Ma, 
      
      Yanming Shen | While Large Language Models (LLMs) dominate tasks like natural language processing and computer vision, harnessing their power for spatial-temporal forecasting remains challenging. The disparity between sequential text and complex spatial-temporal data hinders this application. To address this issue, this paper introduces STG-LLM, an innovative approach empowering LLMs for spatial-temporal forecasting. We tackle the data mismatch by proposing: 1) STG-Tokenizer: This spatial-temporal graph tokenizer transforms intricate graph data into concise tokens capturing both spatial and temporal relationships; 2) STG-Adapter: This minimalistic adapter, consisting of linear encoding and decoding layers, bridges the gap between tokenized data and LLM comprehension. By fine-tuning only a small set of parameters, it can effectively grasp the semantics of tokens generated by STG-Tokenizer, while preserving the original natural language understanding capabilities of LLMs. Extensive experiments on diverse spatial-temporal benchmark datasets show that STG-LLM successfully unlocks LLM potential for spatial-temporal forecasting. Remarkably, our approach achieves competitive performance on par with dedicated SOTA methods.
        △ Less | Computer Vision |
| FP6-LLM: Efficiently Serving Large Language Models Through FP6-Centric Algorithm-System Co-Design | Authors:
Haojun Xia, 
      
      Zhen Zheng, 
      
      Xiaoxia Wu, 
      
      Shiyang Chen, 
      
      Zhewei Yao, 
      
      Stephen Youn, 
      
      Arash Bakhtiari, 
      
      Michael Wyatt, 
      
      Donglin Zhuang, 
      
      Zhongzhu Zhou, 
      
      Olatunji Ruwase, 
      
      Yuxiong He, 
      
      Shuaiwen Leon Song | Six-bit quantization (FP6) can effectively reduce the size of large language models (LLMs) and preserve the model quality consistently across varied applications. However, existing systems do not provide Tensor Core support for FP6 quantization and struggle to achieve practical performance improvements during LLM inference. It is challenging to support FP6 quantization on GPUs due to (1) unfriendly memory access of model weights with irregular bit-width and (2) high runtime overhead of weight de-quantization. To address these problems, we propose TC-FPx, the first full-stack GPU kernel design scheme with unified Tensor Core support of float-point weights for various quantization bit-width. We integrate TC-FPx kernel into an existing inference system, providing new end-to-end support (called FP6-LLM) for quantized LLM inference, where better trade-offs between inference cost and model quality are achieved. Experiments show that FP6-LLM enables the inference of LLaMA-70b using only a single GPU, achieving 1.69x-2.65x higher normalized inference throughput than the FP16 baseline. The source code will be publicly available soon.
        △ Less | Unknown |
| Towards Goal-oriented Large Language Model Prompting: A Survey | Authors:
Haochen Li, 
      
      Jonathan Leung, 
      
      Zhiqi Shen | Large Language Models (LLMs) have shown prominent performance in various downstream tasks in which prompt engineering plays a pivotal role in optimizing LLMs' performance. This paper, not as an overview of current prompt engineering methods, aims to highlight the limitation of designing prompts while holding an anthropomorphic assumption that expects LLMs to think like humans. From our review of 35 representative studies, we demonstrate that a goal-oriented prompt formulation, which guides LLMs to follow established human logical thinking, significantly improves the performance of LLMs. Furthermore, We introduce a novel taxonomy that categorizes goal-oriented prompting methods into five interconnected stages and we demonstrate the broad applicability of our framework by summarizing ten applicable tasks. With four future directions proposed, we hope to further emphasize and promote goal-oriented prompt engineering.
        △ Less | Unknown |
| ChatGPT and Human Synergy in Black-Box Testing: A Comparative Analysis | Authors:
Hiroyuki Kirinuki, 
      
      Haruto Tanno | In recent years, large language models (LLMs), such as ChatGPT, have been pivotal in advancing various artificial intelligence applications, including natural language processing and software engineering. A promising yet underexplored area is utilizing LLMs in software testing, particularly in black-box testing. This paper explores the test cases devised by ChatGPT in comparison to those created by human participants. In this study, ChatGPT (GPT-4) and four participants each created black-box test cases for three applications based on specifications written by the authors. The goal was to evaluate the real-world applicability of the proposed test cases, identify potential shortcomings, and comprehend how ChatGPT could enhance human testing strategies. ChatGPT can generate test cases that generally match or slightly surpass those created by human participants in terms of test viewpoint coverage. Additionally, our experiments demonstrated that when ChatGPT cooperates with humans, it can cover considerably more test viewpoints than each can achieve alone, suggesting that collaboration between humans and ChatGPT may be more effective than human pairs working together. Nevertheless, we noticed that the test cases generated by ChatGPT have certain issues that require addressing before use.
        △ Less | Natural Language Processing |
| WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models | Authors:
Hongliang He, 
      
      Wenlin Yao, 
      
      Kaixin Ma, 
      
      Wenhao Yu, 
      
      Yong Dai, 
      
      Hongming Zhang, 
      
      Zhenzhong Lan, 
      
      Dong Yu | The advancement of large language models (LLMs) leads to a new era marked by the development of autonomous applications in the real world, which drives innovation in the creation of advanced web-based agents. Existing web agents typically only handle one input modality and are evaluated only in simplified web simulators or static web snapshots, greatly limiting their applicability in real-world scenarios. To bridge this gap, we introduce WebVoyager, an innovative Large Multimodal Model (LMM) powered web agent that can complete user instructions end-to-end by interacting with real-world websites. Moreover, we propose a new evaluation protocol for web agents to address the challenges of automatic evaluation of open-ended web agent tasks, leveraging the robust multimodal comprehension capabilities of GPT-4V. We create a new benchmark by gathering real-world tasks from 15 widely used websites to evaluate our agents. We show that WebVoyager achieves a 55.7% task success rate, significantly surpassing the performance of both GPT-4 (All Tools) and the WebVoyager (text-only) setups, underscoring the exceptional capability of WebVoyager in practical applications. We found that our proposed automatic evaluation achieves 85.3% agreement with human judgment, paving the way for further development of web agents in a real-world setting.
        △ Less | Unknown |
| Democratizing Fine-grained Visual Recognition with Large Language Models | Authors:
Mingxuan Liu, 
      
      Subhankar Roy, 
      
      Wenjing Li, 
      
      Zhun Zhong, 
      
      Nicu Sebe, 
      
      Elisa Ricci | Identifying subordinate-level categories from images is a longstanding task in computer vision and is referred to as fine-grained visual recognition (FGVR). It has tremendous significance in real-world applications since an average layperson does not excel at differentiating species of birds or mushrooms due to subtle differences among the species. A major bottleneck in developing FGVR systems is caused by the need of high-quality paired expert annotations. To circumvent the need of expert knowledge we propose Fine-grained Semantic Category Reasoning (FineR) that internally leverages the world knowledge of large language models (LLMs) as a proxy in order to reason about fine-grained category names. In detail, to bridge the modality gap between images and LLM, we extract part-level visual attributes from images as text and feed that information to a LLM. Based on the visual attributes and its internal world knowledge the LLM reasons about the subordinate-level category names. Our training-free FineR outperforms several state-of-the-art FGVR and language and vision assistant models and shows promise in working in the wild and in new domains where gathering expert annotation is arduous.
        △ Less | Computer Vision |
| The Calibration Gap between Model and Human Confidence in Large Language Models | Authors:
Mark Steyvers, 
      
      Heliodoro Tejeda, 
      
      Aakriti Kumar, 
      
      Catarina Belem, 
      
      Sheer Karny, 
      
      Xinyue Hu, 
      
      Lukas Mayer, 
      
      Padhraic Smyth | For large language models (LLMs) to be trusted by humans they need to be well-calibrated in the sense that they can accurately assess and communicate how likely it is that their predictions are correct. Recent work has focused on the quality of internal LLM confidence assessments, but the question remains of how well LLMs can communicate this internal model confidence to human users. This paper explores the disparity between external human confidence in an LLM's responses and the internal confidence of the model. Through experiments involving multiple-choice questions, we systematically examine human users' ability to discern the reliability of LLM outputs. Our study focuses on two key areas: (1) assessing users' perception of true LLM confidence and (2) investigating the impact of tailored explanations on this perception. The research highlights that default explanations from LLMs often lead to user overestimation of both the model's confidence and its' accuracy. By modifying the explanations to more accurately reflect the LLM's internal confidence, we observe a significant shift in user perception, aligning it more closely with the model's actual confidence levels. This adjustment in explanatory approach demonstrates potential for enhancing user trust and accuracy in assessing LLM outputs. The findings underscore the importance of transparent communication of confidence levels in LLMs, particularly in high-stakes applications where understanding the reliability of AI-generated information is essential.
        △ Less | Unknown |
| Synergizing Human Expertise and AI Efficiency with Language Model for Microscopy Operation and Automated Experiment Design | Authors:
Yongtao Liu, 
      
      Marti Checa, 
      
      Rama K. Vasudevan | With the advent of large language models (LLMs), in both the open source and proprietary domains, attention is turning to how to exploit such artificial intelligence (AI) systems in assisting complex scientific tasks, such as material synthesis, characterization, analysis and discovery. Here, we explore the utility of LLM, particularly ChatGPT4, in combination with application program interfaces (APIs) in tasks of experimental design, programming workflows, and data analysis in scanning probe microscopy, using both in-house developed API and API given by a commercial vendor for instrument control. We find that the LLM can be especially useful in converting ideations of experimental workflows to executable code on microscope APIs. Beyond code generation, we find that the GPT4 is capable of analyzing microscopy images in a generic sense. At the same time, we find that GPT4 suffers from inability to extend beyond basic analyses or more in-depth technical experimental design. We argue that a LLM specifically fine-tuned for individual scientific domains can potentially be a better language interface for converting scientific ideations from human experts to executable workflows, such a synergy between human expertise and LLM efficiency in experimentation can open new door for accelerating scientific research, enabling effective experimental protocols archive and sharing in scientific community.
        △ Less | Unknown |
| Investigating the Efficacy of Large Language Models for Code Clone Detection | Authors:
Mohamad Khajezade, 
      
      Jie Wu, 
      
      Fatemeh Hendijani Fard, 
      
      Gema Rodríguez-Pérez, 
      
      Mohamed Sami Shehata | Large Language Models (LLMs) have demonstrated remarkable success in various natural language processing and software engineering tasks, such as code generation. The LLMs are mainly utilized in the prompt-based zero/few-shot paradigm to guide the model in accomplishing the task. %\textbf{Goal:} GPT-based models are one of the popular ones studied for tasks such as code comment generation or test generation. These tasks are `generative' tasks. However, there is limited research on the usage of LLMs for `non-generative' tasks such as classification using the prompt-based paradigm. In this preliminary exploratory study, we investigated the applicability of LLMs for Code Clone Detection (CCD), a non-generative task. %\textbf{Method:} By building a mono-lingual and cross-lingual CCD dataset derived from CodeNet, we first investigated two different prompts using ChatGPT to detect \textcolor{black}{Type-4} code clones in Java-Java and Java-Ruby pairs in a zero-shot setting. We \textcolor{black}{then} conducted an analysis to understand the strengths and weaknesses of ChatGPT in CCD. %\textbf{Results:} ChatGPT surpasses the baselines in cross-language CCD \textcolor{black}{attaining an F1-score of 0.877 } and achieves comparable performance to fully fine-tuned models for mono-lingual CCD, \textcolor{black}{with an F1-score of 0.878}. Also, the \textcolor{black}{prompt and the} difficulty level of the problems has an impact on the performance of ChatGPT. \textcolor{black}{Finally,} we provide insights and future directions based on our initial analysis
        △ Less | Natural Language Processing |
| Evaluation of General Large Language Models in Contextually Assessing Semantic Concepts Extracted from Adult Critical Care Electronic Health Record Notes | Authors:
Darren Liu, 
      
      Cheng Ding, 
      
      Delgersuren Bold, 
      
      Monique Bouvier, 
      
      Jiaying Lu, 
      
      Benjamin Shickel, 
      
      Craig S. Jabaley, 
      
      Wenhui Zhang, 
      
      Soojin Park, 
      
      Michael J. Young, 
      
      Mark S. Wainwright, 
      
      Gilles Clermont, 
      
      Parisa Rashidi, 
      
      Eric S. Rosenthal, 
      
      Laurie Dimisko, 
      
      Ran Xiao, 
      
      Joo Heung Yoon, 
      
      Carl Yang, 
      
      Xiao Hu | The field of healthcare has increasingly turned its focus towards Large Language Models (LLMs) due to their remarkable performance. However, their performance in actual clinical applications has been underexplored. Traditional evaluations based on question-answering tasks don't fully capture the nuanced contexts. This gap highlights the need for more in-depth and practical assessments of LLMs in real-world healthcare settings. Objective: We sought to evaluate the performance of LLMs in the complex clinical context of adult critical care medicine using systematic and comprehensible analytic methods, including clinician annotation and adjudication. Methods: We investigated the performance of three general LLMs in understanding and processing real-world clinical notes. Concepts from 150 clinical notes were identified by MetaMap and then labeled by 9 clinicians. Each LLM's proficiency was evaluated by identifying the temporality and negation of these concepts using different prompts for an in-depth analysis. Results: GPT-4 showed overall superior performance compared to other LLMs. In contrast, both GPT-3.5 and text-davinci-003 exhibit enhanced performance when the appropriate prompting strategies are employed. The GPT family models have demonstrated considerable efficiency, evidenced by their cost-effectiveness and time-saving capabilities. Conclusion: A comprehensive qualitative performance evaluation framework for LLMs is developed and operationalized. This framework goes beyond singular performance aspects. With expert annotations, this methodology not only validates LLMs' capabilities in processing complex medical data but also establishes a benchmark for future LLM evaluations across specialized domains.
        △ Less | Unknown |
| Clue-Guided Path Exploration: An Efficient Knowledge Base Question-Answering Framework with Low Computational Resource Consumption | Authors:
Dehao Tao, 
      
      Feng Huang, 
      
      Yongfeng Huang, 
      
      Minghu Jiang | In recent times, large language models (LLMs) have showcased remarkable capabilities. However, updating their knowledge poses challenges, potentially leading to inaccuracies when confronted with unfamiliar queries. While integrating knowledge graphs with LLMs has been explored, existing approaches treat LLMs as primary decision-makers, imposing high demands on their capabilities. This is particularly unsuitable for LLMs with lower computational costs and relatively poorer performance. In this paper, we introduce a Clue-Guided Path Exploration framework (CGPE) that efficiently merges a knowledge base with an LLM, placing less stringent requirements on the model's capabilities. Inspired by the method humans use to manually retrieve knowledge, CGPE employs information from the question as clues to systematically explore the required knowledge path within the knowledge base. Experiments on open-source datasets reveal that CGPE outperforms previous methods and is highly applicable to LLMs with fewer parameters. In some instances, even ChatGLM3, with its 6 billion parameters, can rival the performance of GPT-4. Furthermore, the results indicate a minimal invocation frequency of CGPE on LLMs, suggesting reduced computational overhead. For organizations and individuals facing constraints in computational resources, our research offers significant practical value.
        △ Less | Unknown |
| Can AI Assistants Know What They Don't Know? | Authors:
Qinyuan Cheng, 
      
      Tianxiang Sun, 
      
      Xiangyang Liu, 
      
      Wenwei Zhang, 
      
      Zhangyue Yin, 
      
      Shimin Li, 
      
      Linyang Li, 
      
      Kai Chen, 
      
      Xipeng Qiu | Recently, AI assistants based on large language models (LLMs) show surprising performance in many tasks, such as dialogue, solving math problems, writing code, and using tools. Although LLMs possess intensive world knowledge, they still make factual errors when facing some knowledge intensive tasks, like open-domain question answering. These untruthful responses from the AI assistant may cause significant risks in practical applications. We believe that an AI assistant's refusal to answer questions it does not know is a crucial method for reducing hallucinations and making the assistant truthful. Therefore, in this paper, we ask the question "Can AI assistants know what they don't know and express them through natural language?" To answer this question, we construct a model-specific "I don't know" (Idk) dataset for an assistant, which contains its known and unknown questions, based on existing open-domain question answering datasets. Then we align the assistant with its corresponding Idk dataset and observe whether it can refuse to answer its unknown questions after alignment. Experimental results show that after alignment with Idk datasets, the assistant can refuse to answer most its unknown questions. For questions they attempt to answer, the accuracy is significantly higher than before the alignment.
        △ Less | Unknown |
| SpecLLM: Exploring Generation and Review of VLSI Design Specification with Large Language Model | Authors:
Mengming Li, 
      
      Wenji Fang, 
      
      Qijun Zhang, 
      
      Zhiyao Xie | The development of architecture specifications is an initial and fundamental stage of the integrated circuit (IC) design process. Traditionally, architecture specifications are crafted by experienced chip architects, a process that is not only time-consuming but also error-prone. Mistakes in these specifications may significantly affect subsequent stages of chip design. Despite the presence of advanced electronic design automation (EDA) tools, effective solutions to these specification-related challenges remain scarce. Since writing architecture specifications is naturally a natural language processing (NLP) task, this paper pioneers the automation of architecture specification development with the advanced capabilities of large language models (LLMs). Leveraging our definition and dataset, we explore the application of LLMs in two key aspects of architecture specification development: (1) Generating architecture specifications, which includes both writing specifications from scratch and converting RTL code into detailed specifications. (2) Reviewing existing architecture specifications. We got promising results indicating that LLMs may revolutionize how these critical specification documents are developed in IC design nowadays. By reducing the effort required, LLMs open up new possibilities for efficiency and accuracy in this crucial aspect of chip design.
        △ Less | Natural Language Processing |
| GraphiMind: LLM-centric Interface for Information Graphics Design | Authors:
Qirui Huang, 
      
      Min Lu, 
      
      Joel Lanir, 
      
      Dani Lischinski, 
      
      Daniel Cohen-Or, 
      
      Hui Huang | Information graphics are pivotal in effective information dissemination and storytelling. However, creating such graphics is extremely challenging for non-professionals, since the design process requires multifaceted skills and comprehensive knowledge. Thus, despite the many available authoring tools, a significant gap remains in enabling non-experts to produce compelling information graphics seamlessly, especially from scratch. Recent breakthroughs show that Large Language Models (LLMs), especially when tool-augmented, can autonomously engage with external tools, making them promising candidates for enabling innovative graphic design applications. In this work, we propose a LLM-centric interface with the agent GraphiMind for automatic generation, recommendation, and composition of information graphics design resources, based on user intent expressed through natural language. Our GraphiMind integrates a Textual Conversational Interface, powered by tool-augmented LLM, with a traditional Graphical Manipulation Interface, streamlining the entire design process from raw resource curation to composition and refinement. Extensive evaluations highlight our tool's proficiency in simplifying the design process, opening avenues for its use by non-professional users. Moreover, we spotlight the potential of LLMs in reshaping the domain of information graphics design, offering a blend of automation, versatility, and user-centric interactivity.
        △ Less | Unknown |
| AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents | Authors:
Chang Ma, 
      
      Junlei Zhang, 
      
      Zhihao Zhu, 
      
      Cheng Yang, 
      
      Yujiu Yang, 
      
      Yaohui Jin, 
      
      Zhenzhong Lan, 
      
      Lingpeng Kong, 
      
      Junxian He | Evaluating large language models (LLMs) as general-purpose agents is essential for understanding their capabilities and facilitating their integration into practical applications. However, the evaluation process presents substantial challenges. A primary obstacle is the benchmarking of agent performance across diverse scenarios within a unified framework, especially in maintaining partially-observable environments and ensuring multi-round interactions. Moreover, current evaluation frameworks mostly focus on the final success rate, revealing few insights during the process and failing to provide a deep understanding of the model abilities. To address these challenges, we introduce AgentBoard, a pioneering comprehensive benchmark and accompanied open-source evaluation framework tailored to analytical evaluation of LLM agents. AgentBoard offers a fine-grained progress rate metric that captures incremental advancements as well as a comprehensive evaluation toolkit that features easy assessment of agents for multi-faceted analysis through interactive visualization. This not only sheds light on the capabilities and limitations of LLM agents but also propels the interpretability of their performance to the forefront. Ultimately, AgentBoard serves as a significant step towards demystifying agent behaviors and accelerating the development of stronger LLM agents.
        △ Less | Unknown |
| XAI for All: Can Large Language Models Simplify Explainable AI? | Authors:
Philip Mavrepis, 
      
      Georgios Makridis, 
      
      Georgios Fatouros, 
      
      Vasileios Koukos, 
      
      Maria Margarita Separdani, 
      
      Dimosthenis Kyriazis | The field of Explainable Artificial Intelligence (XAI) often focuses on users with a strong technical background, making it challenging for non-experts to understand XAI methods. This paper presents "x-[plAIn]", a new approach to make XAI more accessible to a wider audience through a custom Large Language Model (LLM), developed using ChatGPT Builder. Our goal was to design a model that can generate clear, concise summaries of various XAI methods, tailored for different audiences, including business professionals and academics. The key feature of our model is its ability to adapt explanations to match each audience group's knowledge level and interests. Our approach still offers timely insights, facilitating the decision-making process by the end users. Results from our use-case studies show that our model is effective in providing easy-to-understand, audience-specific explanations, regardless of the XAI method used. This adaptability improves the accessibility of XAI, bridging the gap between complex AI technologies and their practical applications. Our findings indicate a promising direction for LLMs in making advanced AI concepts more accessible to a diverse range of users.
        △ Less | Unknown |
| Evaluating and Enhancing Large Language Models Performance in Domain-specific Medicine: Osteoarthritis Management with DocOA | Authors:
Xi Chen, 
      
      MingKe You, 
      
      Li Wang, 
      
      WeiZhi Liu, 
      
      Yu Fu, 
      
      Jie Xu, 
      
      Shaoting Zhang, 
      
      Gang Chen, 
      
      Kang Li, 
      
      Jian Li | The efficacy of large language models (LLMs) in domain-specific medicine, particularly for managing complex diseases such as osteoarthritis (OA), remains largely unexplored. This study focused on evaluating and enhancing the clinical capabilities of LLMs in specific domains, using osteoarthritis (OA) management as a case study. A domain specific benchmark framework was developed, which evaluate LLMs across a spectrum from domain-specific knowledge to clinical applications in real-world clinical scenarios. DocOA, a specialized LLM tailored for OA management that integrates retrieval-augmented generation (RAG) and instruction prompts, was developed. The study compared the performance of GPT-3.5, GPT-4, and a specialized assistant, DocOA, using objective and human evaluations. Results showed that general LLMs like GPT-3.5 and GPT-4 were less effective in the specialized domain of OA management, particularly in providing personalized treatment recommendations. However, DocOA showed significant improvements. This study introduces a novel benchmark framework which assesses the domain-specific abilities of LLMs in multiple aspects, highlights the limitations of generalized LLMs in clinical contexts, and demonstrates the potential of tailored approaches for developing domain-specific medical LLMs.
        △ Less | Unknown |
| A General-purpose AI Avatar in Healthcare | Authors:
Nicholas Yan, 
      
      Gil Alterovitz | Recent advancements in machine learning and natural language processing have led to the rapid development of artificial intelligence (AI) as a valuable tool in the healthcare industry. Using large language models (LLMs) as conversational agents or chatbots has the potential to assist doctors in diagnosing patients, detecting early symptoms of diseases, and providing health advice to patients. This paper focuses on the role of chatbots in healthcare and explores the use of avatars to make AI interactions more appealing to patients. A framework of a general-purpose AI avatar application is demonstrated by using a three-category prompt dictionary and prompt improvement mechanism. A two-phase approach is suggested to fine-tune a general-purpose AI language model and create different AI avatars to discuss medical issues with users. Prompt engineering enhances the chatbot's conversational abilities and personality traits, fostering a more human-like interaction with patients. Ultimately, the injection of personality into the chatbot could potentially increase patient engagement. Future directions for research include investigating ways to improve chatbots' understanding of context and ensuring the accuracy of their outputs through fine-tuning with specialized medical data sets.
        △ Less | Machine Learning |
| Chatterbox: Robust Transport for LLM Token Streaming under Unstable Network | Authors:
Hanchen Li, 
      
      Yuhan Liu, 
      
      Yihua Cheng, 
      
      Siddhant Ray, 
      
      Kuntai Du, 
      
      Junchen Jiang | To render each generated token in real time, the LLM server generates response tokens one by one and streams each generated token (or group of a few tokens) through the network to the user right after it is generated, which we refer to as LLM token streaming. However, under unstable network conditions, the LLM token streaming experience could suffer greatly from stalls since one packet loss could block the rendering of tokens contained in subsequent packets even if they arrive on time. With a real-world measurement study, we show that current applications including ChatGPT, Claude, and Bard all suffer from increased stall under unstable network.
  For this emerging token streaming problem in LLM Chatbots, we propose a novel transport layer scheme, called Chatterbox, which puts new generated tokens as well as currently unacknowledged tokens in the next outgoing packet. This ensures that each packet contains some new tokens and can be independently rendered when received, thus avoiding aforementioned stalls caused by missing packets. Through simulation under various network conditions, we show Chatterbox reduces stall ratio (proportion of token rendering wait time) by 71.0% compared to the token streaming method commonly used by real chatbot applications and by 31.6% compared to a custom packet duplication scheme. By tailoring Chatterbox to fit the token-by-token generation of LLM, we enable the Chatbots to respond like an eloquent speaker for users to better enjoy pervasive AI.
        △ Less | Unknown |
| From Understanding to Utilization: A Survey on Explainability for Large Language Models | Authors:
Haoyan Luo, 
      
      Lucia Specia | This survey paper delves into the burgeoning field of explainability for Large Language Models (LLMs), a critical yet challenging aspect of natural language processing. With LLMs playing a pivotal role in various applications, their "black-box" nature raises concerns about transparency and ethical use. This paper emphasizes the necessity for enhanced explainability in LLMs, addressing both the general public's trust and the technical community's need for a deeper understanding of these models. We concentrate on pre-trained Transformer-based LLMs, such as LLaMA, which present unique interpretability challenges due to their scale and complexity. Our review categorizes existing explainability methods and discusses their application in improving model transparency and reliability. We also discuss representative evaluation methods, highlighting their strengths and limitations. The goal of this survey is to bridge the gap between theoretical understanding and practical application, offering insights for future research and development in the field of LLM explainability.
        △ Less | Natural Language Processing |
| ChatGraph: Chat with Your Graphs | Authors:
Yun Peng, 
      
      Sen Lin, 
      
      Qian Chen, 
      
      Lyu Xu, 
      
      Xiaojun Ren, 
      
      Yafei Li, 
      
      Jianliang Xu | Graph analysis is fundamental in real-world applications. Traditional approaches rely on SPARQL-like languages or clicking-and-dragging interfaces to interact with graph data. However, these methods either require users to possess high programming skills or support only a limited range of graph analysis functionalities. To address the limitations, we propose a large language model (LLM)-based framework called ChatGraph. With ChatGraph, users can interact with graphs through natural language, making it easier to use and more flexible than traditional approaches. The core of ChatGraph lies in generating chains of graph analysis APIs based on the understanding of the texts and graphs inputted in the user prompts. To achieve this, ChatGraph consists of three main modules: an API retrieval module that searches for relevant APIs, a graph-aware LLM module that enables the LLM to comprehend graphs, and an API chain-oriented finetuning module that guides the LLM in generating API chains.
        △ Less | Unknown |
| Automated Fact-Checking of Climate Change Claims with Large Language Models | Authors:
Markus Leippold, 
      
      Saeid Ashraf Vaghefi, 
      
      Dominik Stammbach, 
      
      Veruska Muccione, 
      
      Julia Bingler, 
      
      Jingwei Ni, 
      
      Chiara Colesanti-Senni, 
      
      Tobias Wekhof, 
      
      Tobias Schimanski, 
      
      Glen Gostlow, 
      
      Tingyu Yu, 
      
      Juerg Luterbacher, 
      
      Christian Huggel | This paper presents Climinator, a novel AI-based tool designed to automate the fact-checking of climate change claims. Utilizing an array of Large Language Models (LLMs) informed by authoritative sources like the IPCC reports and peer-reviewed scientific literature, Climinator employs an innovative Mediator-Advocate framework. This design allows Climinator to effectively synthesize varying scientific perspectives, leading to robust, evidence-based evaluations. Our model demonstrates remarkable accuracy when testing claims collected from Climate Feedback and Skeptical Science. Notably, when integrating an advocate with a climate science denial perspective in our framework, Climinator's iterative debate process reliably converges towards scientific consensus, underscoring its adeptness at reconciling diverse viewpoints into science-based, factual conclusions. While our research is subject to certain limitations and necessitates careful interpretation, our approach holds significant potential. We hope to stimulate further research and encourage exploring its applicability in other contexts, including political fact-checking and legal domains.
        △ Less | Unknown |
| Assessing and Understanding Creativity in Large Language Models | Authors:
Yunpu Zhao, 
      
      Rui Zhang, 
      
      Wenyi Li, 
      
      Di Huang, 
      
      Jiaming Guo, 
      
      Shaohui Peng, 
      
      Yifan Hao, 
      
      Yuanbo Wen, 
      
      Xing Hu, 
      
      Zidong Du, 
      
      Qi Guo, 
      
      Ling Li, 
      
      Yunji Chen | In the field of natural language processing, the rapid development of large language model (LLM) has attracted more and more attention. LLMs have shown a high level of creativity in various tasks, but the methods for assessing such creativity are inadequate. The assessment of LLM creativity needs to consider differences from humans, requiring multi-dimensional measurement while balancing accuracy and efficiency. This paper aims to establish an efficient framework for assessing the level of creativity in LLMs. By adapting the modified Torrance Tests of Creative Thinking, the research evaluates the creative performance of various LLMs across 7 tasks, emphasizing 4 criteria including Fluency, Flexibility, Originality, and Elaboration. In this context, we develop a comprehensive dataset of 700 questions for testing and an LLM-based evaluation method. In addition, this study presents a novel analysis of LLMs' responses to diverse prompts and role-play situations. We found that the creativity of LLMs primarily falls short in originality, while excelling in elaboration. Besides, the use of prompts and the role-play settings of the model significantly influence creativity. Additionally, the experimental results also indicate that collaboration among multiple LLMs can enhance originality. Notably, our findings reveal a consensus between human evaluations and LLMs regarding the personality traits that influence creativity. The findings underscore the significant impact of LLM design on creativity and bridges artificial intelligence and human creativity, offering insights into LLMs' creativity and potential applications.
        △ Less | Natural Language Processing |
| GRATH: Gradual Self-Truthifying for Large Language Models | Authors:
Weixin Chen, 
      
      Bo Li | Truthfulness is paramount for large language models (LLMs) as they are increasingly deployed in real-world applications. However, existing LLMs still struggle with generating truthful answers and content, as evidenced by their modest performance on benchmarks like TruthfulQA. To address this issue, we propose GRAdual self-truTHifying (GRATH), a novel post-processing method to enhance truthfulness of LLMs. GRATH utilizes out-of-domain question prompts to generate corresponding answers and adaptively optimizes the model via direct preference optimization (DPO). Note that during this process, GRATH learns truthfulness in a self-supervised manner without requiring annotated answers. In particular, GRATH first generates pairwise truthfulness training data by prompting the LLM itself, with each pair containing a question and its correct and incorrect answers. The model is then fine-tuned using DPO to learn from the difference between answer pairs. Subsequently, GRATH iteratively refines the truthfulness data and optimizes the model, leading to a gradual improvement in model truthfulness. Empirically, we evaluate GRATH using different 7B-LLMs and compare with LLMs with similar or even larger sizes on benchmark datasets. Our results show that GRATH effectively improves LLMs' truthfulness without compromising other core capabilities. Notably, GRATH achieves state-of-the-art performance on TruthfulQA, with MC1 accuracy as 54.71% and MC2 accuracy as 69.10%, which even surpass those on larger-scale models, such as Llama2-Chat-70B, by 23.62% and 24.18%, respectively.
        △ Less | Unknown |
| LLM4EDA: Emerging Progress in Large Language Models for Electronic Design Automation | Authors:
Ruizhe Zhong, 
      
      Xingbo Du, 
      
      Shixiong Kai, 
      
      Zhentao Tang, 
      
      Siyuan Xu, 
      
      Hui-Ling Zhen, 
      
      Jianye Hao, 
      
      Qiang Xu, 
      
      Mingxuan Yuan, 
      
      Junchi Yan | Driven by Moore's Law, the complexity and scale of modern chip design are increasing rapidly. Electronic Design Automation (EDA) has been widely applied to address the challenges encountered in the full chip design process. However, the evolution of very large-scale integrated circuits has made chip design time-consuming and resource-intensive, requiring substantial prior expert knowledge. Additionally, intermediate human control activities are crucial for seeking optimal solutions. In system design stage, circuits are usually represented with Hardware Description Language (HDL) as a textual format. Recently, Large Language Models (LLMs) have demonstrated their capability in context understanding, logic reasoning and answer generation. Since circuit can be represented with HDL in a textual format, it is reasonable to question whether LLMs can be leveraged in the EDA field to achieve fully automated chip design and generate circuits with improved power, performance, and area (PPA). In this paper, we present a systematic study on the application of LLMs in the EDA field, categorizing it into the following cases: 1) assistant chatbot, 2) HDL and script generation, and 3) HDL verification and analysis. Additionally, we highlight the future research direction, focusing on applying LLMs in logic synthesis, physical design, multi-modal feature extraction and alignment of circuits. We collect relevant papers up-to-date in this field via the following link: https://github.com/Thinklab-SJTU/Awesome-LLM4EDA.
        △ Less | Unknown |
| The Curious Case of Nonverbal Abstract Reasoning with Multi-Modal Large Language Models | Authors:
Kian Ahrabian, 
      
      Zhivar Sourati, 
      
      Kexuan Sun, 
      
      Jiarui Zhang, 
      
      Yifan Jiang, 
      
      Fred Morstatter, 
      
      Jay Pujara | While large language models (LLMs) are still being adopted to new domains and utilized in novel applications, we are experiencing an influx of the new generation of foundation models, namely multi-modal large language models (MLLMs). These models integrate verbal and visual information, opening new possibilities to demonstrate more complex reasoning abilities at the intersection of the two modalities. However, despite the revolutionizing prospect of MLLMs, our understanding of their reasoning abilities is limited. In this study, we assess the nonverbal abstract reasoning abilities of open-source and closed-source MLLMs using variations of Raven's Progressive Matrices. Our experiments expose the difficulty of solving such problems while showcasing the immense gap between open-source and closed-source models. We also reveal critical shortcomings with individual visual and textual modules, subjecting the models to low-performance ceilings. Finally, to improve MLLMs' performance, we experiment with various methods, such as Chain-of-Thought prompting, resulting in a significant (up to 100%) boost in performance.
        △ Less | Unknown |
| An Empirical Analysis of In-context Learning Abilities of LLMs for MT | Authors:
Pranjal A. Chitale, 
      
      Jay Gala, 
      
      Varun Gumma, 
      
      Mitesh M. Khapra, 
      
      Raj Dabre | In-context learning (ICL) has consistently demonstrated superior performance over zero-shot performance in large language models (LLMs). However, the understanding of the dynamics of ICL and the aspects that influence downstream performance remains limited, especially for natural language generation (NLG) tasks. This work aims to address this gap by investigating the ICL capabilities of LLMs and studying the impact of different aspects of the in-context demonstrations for the task of machine translation (MT). Our preliminary investigations aim to discern whether in-context learning (ICL) is predominantly influenced by demonstrations or instructions by applying diverse perturbations to in-context demonstrations while preserving the task instruction. We observe varying behavior to perturbed examples across different model families, notably with BLOOM-7B derivatives being severely influenced by noise, whereas Llama 2 derivatives not only exhibit robustness but also tend to show enhancements over the clean baseline when subject to perturbed demonstrations. This suggests that the robustness of ICL may be governed by several factors, including the type of noise, perturbation direction (source or target), the extent of pretraining of the specific model, and fine-tuning for downstream tasks if applicable. Further investigation is warranted to develop a comprehensive understanding of these factors in future research.
        △ Less | Unknown |
| AI for social science and social science of AI: A Survey | Authors:
Ruoxi Xu, 
      
      Yingfei Sun, 
      
      Mengjie Ren, 
      
      Shiguang Guo, 
      
      Ruotong Pan, 
      
      Hongyu Lin, 
      
      Le Sun, 
      
      Xianpei Han | Recent advancements in artificial intelligence, particularly with the emergence of large language models (LLMs), have sparked a rethinking of artificial general intelligence possibilities. The increasing human-like capabilities of AI are also attracting attention in social science research, leading to various studies exploring the combination of these two fields. In this survey, we systematically categorize previous explorations in the combination of AI and social science into two directions that share common technical approaches but differ in their research objectives. The first direction is focused on AI for social science, where AI is utilized as a powerful tool to enhance various stages of social science research. While the second direction is the social science of AI, which examines AI agents as social entities with their human-like cognitive and linguistic capabilities. By conducting a thorough review, particularly on the substantial progress facilitated by recent advancements in large language models, this paper introduces a fresh perspective to reassess the relationship between AI and social science, provides a cohesive framework that allows researchers to understand the distinctions and connections between AI for social science and social science of AI, and also summarized state-of-art experiment simulation platforms to facilitate research in these two directions. We believe that as AI technology continues to advance and intelligent agents find increasing applications in our daily lives, the significance of the combination of AI and social science will become even more prominent.
        △ Less | Unknown |
| The Conversation is the Command: Interacting with Real-World Autonomous Robot Through Natural Language | Authors:
Linus Nwankwo, 
      
      Elmar Rueckert | In recent years, autonomous agents have surged in real-world environments such as our homes, offices, and public spaces. However, natural human-robot interaction remains a key challenge. In this paper, we introduce an approach that synergistically exploits the capabilities of large language models (LLMs) and multimodal vision-language models (VLMs) to enable humans to interact naturally with autonomous robots through conversational dialogue. We leveraged the LLMs to decode the high-level natural language instructions from humans and abstract them into precise robot actionable commands or queries. Further, we utilised the VLMs to provide a visual and semantic understanding of the robot's task environment. Our results with 99.13% command recognition accuracy and 97.96% commands execution success show that our approach can enhance human-robot interaction in real-world applications. The video demonstrations of this paper can be found at https://osf.io/wzyf6 and the code is available at our GitHub repository (https://github.com/LinusNEP/TCC_IRoNL.git).
        △ Less | Unknown |
| Revolutionizing Finance with LLMs: An Overview of Applications and Insights | Authors:
Huaqin Zhao, 
      
      Zhengliang Liu, 
      
      Zihao Wu, 
      
      Yiwei Li, 
      
      Tianze Yang, 
      
      Peng Shu, 
      
      Shaochen Xu, 
      
      Haixing Dai, 
      
      Lin Zhao, 
      
      Gengchen Mai, 
      
      Ninghao Liu, 
      
      Tianming Liu | In recent years, Large Language Models (LLMs) like ChatGPT have seen considerable advancements and have been applied in diverse fields. Built on the Transformer architecture, these models are trained on extensive datasets, enabling them to understand and generate human language effectively. In the financial domain, the deployment of LLMs is gaining momentum. These models are being utilized for automating financial report generation, forecasting market trends, analyzing investor sentiment, and offering personalized financial advice. Leveraging their natural language processing capabilities, LLMs can distill key insights from vast financial data, aiding institutions in making informed investment choices and enhancing both operational efficiency and customer satisfaction. In this study, we provide a comprehensive overview of the emerging integration of LLMs into various financial tasks. Additionally, we conducted holistic tests on multiple financial tasks through the combination of natural language instructions. Our findings show that GPT-4 effectively follow prompt instructions across various financial tasks. This survey and evaluation of LLMs in the financial domain aim to deepen the understanding of LLMs' current role in finance for both financial practitioners and LLM researchers, identify new research and application prospects, and highlight how these technologies can be leveraged to solve practical challenges in the finance industry.
        △ Less | Natural Language Processing |
| Integration of Large Language Models in Control of EHD Pumps for Precise Color Synthesis | Authors:
Yanhong Peng, 
      
      Ceng Zhang, 
      
      Chenlong Hu, 
      
      Zebing Mao | This paper presents an innovative approach to integrating Large Language Models (LLMs) with Arduino-controlled Electrohydrodynamic (EHD) pumps for precise color synthesis in automation systems. We propose a novel framework that employs fine-tuned LLMs to interpret natural language commands and convert them into specific operational instructions for EHD pump control. This approach aims to enhance user interaction with complex hardware systems, making it more intuitive and efficient. The methodology involves four key steps: fine-tuning the language model with a dataset of color specifications and corresponding Arduino code, developing a natural language processing interface, translating user inputs into executable Arduino code, and controlling EHD pumps for accurate color mixing. Conceptual experiment results, based on theoretical assumptions, indicate a high potential for accurate color synthesis, efficient language model interpretation, and reliable EHD pump operation. This research extends the application of LLMs beyond text-based tasks, demonstrating their potential in industrial automation and control systems. While highlighting the limitations and the need for real-world testing, this study opens new avenues for AI applications in physical system control and sets a foundation for future advancements in AI-driven automation technologies.
        △ Less | Natural Language Processing |
| Linear Alignment: A Closed-form Solution for Aligning Human Preferences without Tuning and Feedback | Authors:
Songyang Gao, 
      
      Qiming Ge, 
      
      Wei Shen, 
      
      Shihan Dou, 
      
      Junjie Ye, 
      
      Xiao Wang, 
      
      Rui Zheng, 
      
      Yicheng Zou, 
      
      Zhi Chen, 
      
      Hang Yan, 
      
      Qi Zhang, 
      
      Dahua Lin | The success of AI assistants based on Language Models (LLMs) hinges on Reinforcement Learning from Human Feedback (RLHF) to comprehend and align with user intentions. However, traditional alignment algorithms, such as PPO, are hampered by complex annotation and training requirements. This reliance limits the applicability of RLHF and hinders the development of professional assistants tailored to diverse human preferences. In this work, we introduce \textit{Linear Alignment}, a novel algorithm that aligns language models with human preferences in one single inference step, eliminating the reliance on data annotation and model training. Linear alignment incorporates a new parameterization for policy optimization under divergence constraints, which enables the extraction of optimal policy in a closed-form manner and facilitates the direct estimation of the aligned response. Extensive experiments on both general and personalized preference datasets demonstrate that linear alignment significantly enhances the performance and efficiency of LLM alignment across diverse scenarios. Our code and dataset will be published on \url{https://github.com/Wizardcoast/Linear_Alignment.git}.
        △ Less | Unknown |
| MedLM: Exploring Language Models for Medical Question Answering Systems | Authors:
Niraj Yagnik, 
      
      Jay Jhaveri, 
      
      Vivek Sharma, 
      
      Gabriel Pila, 
      
      Asma Ben, 
      
      Jingbo Shang | In the face of rapidly expanding online medical literature, automated systems for aggregating and summarizing information are becoming increasingly crucial for healthcare professionals and patients. Large Language Models (LLMs), with their advanced generative capabilities, have shown promise in various NLP tasks, and their potential in the healthcare domain, particularly for Closed-Book Generative QnA, is significant. However, the performance of these models in domain-specific tasks such as medical Q&A remains largely unexplored. This study aims to fill this gap by comparing the performance of general and medical-specific distilled LMs for medical Q&A. We aim to evaluate the effectiveness of fine-tuning domain-specific LMs and compare the performance of different families of Language Models. The study will address critical questions about these models' reliability, comparative performance, and effectiveness in the context of medical Q&A. The findings will provide valuable insights into the suitability of different LMs for specific applications in the medical domain.
        △ Less | Unknown |
| Prompt-RAG: Pioneering Vector Embedding-Free Retrieval-Augmented Generation in Niche Domains, Exemplified by Korean Medicine | Authors:
Bongsu Kang, 
      
      Jundong Kim, 
      
      Tae-Rim Yun, 
      
      Chang-Eop Kim | We propose a natural language prompt-based retrieval augmented generation (Prompt-RAG), a novel approach to enhance the performance of generative large language models (LLMs) in niche domains. Conventional RAG methods mostly require vector embeddings, yet the suitability of generic LLM-based embedding representations for specialized domains remains uncertain. To explore and exemplify this point, we compared vector embeddings from Korean Medicine (KM) and Conventional Medicine (CM) documents, finding that KM document embeddings correlated more with token overlaps and less with human-assessed document relatedness, in contrast to CM embeddings. Prompt-RAG, distinct from conventional RAG models, operates without the need for embedding vectors. Its performance was assessed through a Question-Answering (QA) chatbot application, where responses were evaluated for relevance, readability, and informativeness. The results showed that Prompt-RAG outperformed existing models, including ChatGPT and conventional vector embedding-based RAGs, in terms of relevance and informativeness. Despite challenges like content structuring and response latency, the advancements in LLMs are expected to encourage the use of Prompt-RAG, making it a promising tool for other domains in need of RAG methods.
        △ Less | Unknown |
| InferAligner: Inference-Time Alignment for Harmlessness through Cross-Model Guidance | Authors:
Pengyu Wang, 
      
      Dong Zhang, 
      
      Linyang Li, 
      
      Chenkun Tan, 
      
      Xinghao Wang, 
      
      Ke Ren, 
      
      Botian Jiang, 
      
      Xipeng Qiu | With the rapid development of large language models (LLMs), they are not only used as general-purpose AI assistants but are also customized through further fine-tuning to meet the requirements of different applications. A pivotal factor in the success of current LLMs is the alignment process. Current alignment methods, such as supervised fine-tuning (SFT) and reinforcement learning from human feedback (RLHF), focus on training-time alignment and are often complex and cumbersome to implement. Therefore, we develop \textbf{InferAligner}, a novel inference-time alignment method that utilizes cross-model guidance for harmlessness alignment. InferAligner utilizes safety steering vectors extracted from safety-aligned model to modify the activations of the target model when responding to harmful inputs, thereby guiding the target model to provide harmless responses. Experimental results show that our method can be very effectively applied to domain-specific models in finance, medicine, and mathematics, as well as to multimodal large language models (MLLMs) such as LLaVA. It significantly diminishes the Attack Success Rate (ASR) of both harmful instructions and jailbreak attacks, while maintaining almost unchanged performance in downstream tasks.
        △ Less | Unknown |
| Enhancing Large Language Models for Clinical Decision Support by Incorporating Clinical Practice Guidelines | Authors:
David Oniani, 
      
      Xizhi Wu, 
      
      Shyam Visweswaran, 
      
      Sumit Kapoor, 
      
      Shravan Kooragayalu, 
      
      Katelyn Polanska, 
      
      Yanshan Wang | Background Large Language Models (LLMs), enhanced with Clinical Practice Guidelines (CPGs), can significantly improve Clinical Decision Support (CDS). However, methods for incorporating CPGs into LLMs are not well studied. Methods We develop three distinct methods for incorporating CPGs into LLMs: Binary Decision Tree (BDT), Program-Aided Graph Construction (PAGC), and Chain-of-Thought-Few-Shot Prompting (CoT-FSP). To evaluate the effectiveness of the proposed methods, we create a set of synthetic patient descriptions and conduct both automatic and human evaluation of the responses generated by four LLMs: GPT-4, GPT-3.5 Turbo, LLaMA, and PaLM 2. Zero-Shot Prompting (ZSP) was used as the baseline method. We focus on CDS for COVID-19 outpatient treatment as the case study. Results All four LLMs exhibit improved performance when enhanced with CPGs compared to the baseline ZSP. BDT outperformed both CoT-FSP and PAGC in automatic evaluation. All of the proposed methods demonstrated high performance in human evaluation. Conclusion LLMs enhanced with CPGs demonstrate superior performance, as compared to plain LLMs with ZSP, in providing accurate recommendations for COVID-19 outpatient treatment, which also highlights the potential for broader applications beyond the case study.
        △ Less | Unknown |
| FAIR Enough: How Can We Develop and Assess a FAIR-Compliant Dataset for Large Language Models' Training? | Authors:
Shaina Raza, 
      
      Shardul Ghuge, 
      
      Chen Ding, 
      
      Deval Pandya | The rapid evolution of Large Language Models (LLMs) underscores the critical importance of ethical considerations and data integrity in AI development, emphasizing the role of FAIR (Findable, Accessible, Interoperable, Reusable) data principles. While these principles have long been a cornerstone of ethical data stewardship, their application in LLM training data is less prevalent, an issue our research aims to address. Our study begins with a review of existing literature, highlighting the significance of FAIR principles in data management for model training. Building on this foundation, we introduce a novel framework that incorporates FAIR principles into the LLM training process. A key aspect of this approach is a comprehensive checklist, designed to assist researchers and developers in consistently applying FAIR data principles throughout the model development lifecycle. The practicality and effectiveness of our framework are demonstrated through a case study that involves creating a FAIR-compliant dataset to detect and reduce biases. This case study not only validates the usefulness of our framework but also establishes new benchmarks for more equitable, transparent, and ethical practices in LLM training. We offer this framework to the community as a means to promote technologically advanced, ethically sound, and socially responsible AI models.
        △ Less | Unknown |
| BioFinBERT: Finetuning Large Language Models (LLMs) to Analyze Sentiment of Press Releases and Financial Text Around Inflection Points of Biotech Stocks | Authors:
Valentina Aparicio, 
      
      Daniel Gordon, 
      
      Sebastian G. Huayamares, 
      
      Yuhuai Luo | Large language models (LLMs) are deep learning algorithms being used to perform natural language processing tasks in various fields, from social sciences to finance and biomedical sciences. Developing and training a new LLM can be very computationally expensive, so it is becoming a common practice to take existing LLMs and finetune them with carefully curated datasets for desired applications in different fields. Here, we present BioFinBERT, a finetuned LLM to perform financial sentiment analysis of public text associated with stocks of companies in the biotechnology sector. The stocks of biotech companies developing highly innovative and risky therapeutic drugs tend to respond very positively or negatively upon a successful or failed clinical readout or regulatory approval of their drug, respectively. These clinical or regulatory results are disclosed by the biotech companies via press releases, which are followed by a significant stock response in many cases. In our attempt to design a LLM capable of analyzing the sentiment of these press releases,we first finetuned BioBERT, a biomedical language representation model designed for biomedical text mining, using financial textual databases. Our finetuned model, termed BioFinBERT, was then used to perform financial sentiment analysis of various biotech-related press releases and financial text around inflection points that significantly affected the price of biotech stocks.
        △ Less | Natural Language Processing |
| Metacognition is all you need? Using Introspection in Generative Agents to Improve Goal-directed Behavior | Authors:
Jason Toy, 
      
      Josh MacAdam, 
      
      Phil Tabor | Recent advances in Large Language Models (LLMs) have shown impressive capabilities in various applications, yet LLMs face challenges such as limited context windows and difficulties in generalization. In this paper, we introduce a metacognition module for generative agents, enabling them to observe their own thought processes and actions. This metacognitive approach, designed to emulate System 1 and System 2 cognitive processes, allows agents to significantly enhance their performance by modifying their strategy. We tested the metacognition module on a variety of scenarios, including a situation where generative agents must survive a zombie apocalypse, and observe that our system outperform others, while agents adapt and improve their strategies to complete tasks over time.
        △ Less | Unknown |
| MLLM-Tool: A Multimodal Large Language Model For Tool Agent Learning | Authors:
Chenyu Wang, 
      
      Weixin Luo, 
      
      Qianyu Chen, 
      
      Haonan Mai, 
      
      Jindi Guo, 
      
      Sixun Dong, 
      
       Xiaohua, 
      
       Xuan, 
      
      Zhengxin Li, 
      
      Lin Ma, 
      
      Shenghua Gao | Recently, the astonishing performance of large language models (LLMs) in natural language comprehension and generation tasks triggered lots of exploration of using them as central controllers to build agent systems. Multiple studies focus on bridging the LLMs to external tools to extend the application scenarios. However, the current LLMs' perceiving tool-use ability is limited to a single text query, which may result in ambiguity in understanding the users' real intentions. LLMs are expected to eliminate that by perceiving the visual- or auditory-grounded instructions' information. Therefore, in this paper, we propose MLLM-Tool, a system incorporating open-source LLMs and multi-modal encoders so that the learnt LLMs can be conscious of multi-modal input instruction and then select the function-matched tool correctly. To facilitate the evaluation of the model's capability, we collect a dataset featured by consisting of multi-modal input tools from HuggingFace. Another important feature of our dataset is that our dataset also contains multiple potential choices for the same instruction due to the existence of identical functions and synonymous functions, which provides more potential solutions for the same query. The experiments reveal that our MLLM-Tool is capable of recommending appropriate tools for multi-modal instructions. Codes and data are available at https://github.com/MLLM-Tool/MLLM-Tool.
        △ Less | Unknown |
| FinSQL: Model-Agnostic LLMs-based Text-to-SQL Framework for Financial Analysis | Authors:
Chao Zhang, 
      
      Yuren Mao, 
      
      Yijiang Fan, 
      
      Yu Mi, 
      
      Yunjun Gao, 
      
      Lu Chen, 
      
      Dongfang Lou, 
      
      Jinshu Lin | Text-to-SQL, which provides zero-code interface for operating relational databases, has gained much attention in financial analysis; because, financial professionals may not well-skilled in SQL programming. However, until now, there is no practical Text-to-SQL benchmark dataset for financial analysis, and existing Text-to-SQL methods have not considered the unique characteristics of databases in financial applications, such as commonly existing wide tables. To address these issues, we collect a practical Text-to-SQL benchmark dataset and propose a model-agnostic Large Language Model (LLMs)-based Text-to-SQL framework for financial analysis. The benchmark dataset, BULL, is collected from the practical financial analysis business of Hundsun Technologies Inc., including databases for fund, stock, and macro economy. Besides, the proposed LLMs-based Text-to-SQL framework, FinSQL, provides a systematic treatment for financial Text-to-SQL from the perspectives of prompt construction, parameter-efficient fine-tuning and output calibration. Extensive experimental results on BULL demonstrate that FinSQL achieves the state-of-the-art Text-to-SQL performance at a small cost; furthermore, FinSQL can bring up to 36.64% performance improvement in scenarios requiring few-shot cross-database model transfer.
        △ Less | Unknown |
| Name Tagging Under Domain Shift via Metric Learning for Life Sciences | Authors:
Hongyi Liu, 
      
      Qingyun Wang, 
      
      Payam Karisani, 
      
      Heng Ji | Name tagging is a key component of Information Extraction (IE), particularly in scientific domains such as biomedicine and chemistry, where large language models (LLMs), e.g., ChatGPT, fall short. We investigate the applicability of transfer learning for enhancing a name tagging model trained in the biomedical domain (the source domain) to be used in the chemical domain (the target domain). A common practice for training such a model in a few-shot learning setting is to pretrain the model on the labeled source data, and then, to finetune it on a hand-full of labeled target examples. In our experiments we observed that such a model is prone to mis-labeling the source entities, which can often appear in the text, as the target entities. To alleviate this problem, we propose a model to transfer the knowledge from the source domain to the target domain, however, at the same time, to project the source entities and target entities into separate regions of the feature space. This diminishes the risk of mis-labeling the source entities as the target entities. Our model consists of two stages: 1) entity grouping in the source domain, which incorporates knowledge from annotated events to establish relations between entities, and 2) entity discrimination in the target domain, which relies on pseudo labeling and contrastive learning to enhance discrimination between the entities in the two domains. We carry out our extensive experiments across three source and three target datasets, and demonstrate that our method outperforms the baselines, in some scenarios by 5\% absolute value.
        △ Less | Unknown |
| Can Large Language Model Summarizers Adapt to Diverse Scientific Communication Goals? | Authors:
Marcio Fonseca, 
      
      Shay B. Cohen | In this work, we investigate the controllability of large language models (LLMs) on scientific summarization tasks. We identify key stylistic and content coverage factors that characterize different types of summaries such as paper reviews, abstracts, and lay summaries. By controlling stylistic features, we find that non-fine-tuned LLMs outperform humans in the MuP review generation task, both in terms of similarity to reference summaries and human preferences. Also, we show that we can improve the controllability of LLMs with keyword-based classifier-free guidance (CFG) while achieving lexical overlap comparable to strong fine-tuned baselines on arXiv and PubMed. However, our results also indicate that LLMs cannot consistently generate long summaries with more than 8 sentences. Furthermore, these models exhibit limited capacity to produce highly abstractive lay summaries. Although LLMs demonstrate strong generic summarization competency, sophisticated content control without costly fine-tuning remains an open problem for domain-specific applications.
        △ Less | Unknown |
