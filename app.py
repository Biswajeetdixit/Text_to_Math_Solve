import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool, initialize_agent
from langchain.callbacks import StreamlitCallbackHandler


groq_api_key="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"
## set upi streamlit app 
st.set_page_config(page_title="Text to Math Problem Solver And D ata Searcg Assistant",page_icon='+ - % *')
st.title("Tex to math Problem Solver using Gemma 2")

groq_api_key=st.sidebar.text_input(lable='Groq Api key',type='password')


if not groq_api_key:
    st.info("Plese enter a groq api key")
    st.stop()

llm=ChatGroq(model="Gemma2-9b-It",groq_api_key=groq_api_key)


Wikipedia_Wrapper=WikipediaAPIWrapper()
wikipedia_tool=Tool(
    name="wikipedia",
    func=Wikipedia_Wrapper.run,
    description="A tool for searching the internet to find the various information"
)

math_chain=LLMMathChain.from_llm(llm=llm)
calculator=Tool(
    name="Calculator",
    func=math_chain.run,
    description="A tools for answaring math related question"

)