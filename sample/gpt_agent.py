from browser_use import Agent
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


def get_agent_for(task: str, model: str = 'gpt-4o-mini'):
    llm = ChatOpenAI(model=model)
    return Agent(task=task, llm=llm)
