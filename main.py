from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAi
from langchain.tools import tool 
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv




# simple tool that is a calculator 
# looks for dotenv
load_dotenv()

def main():
    model = ChatOpenAi(temperature=0)

    tools =[]


    agent_executor = create_react_agent(model,tools)