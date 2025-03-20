from browser_use import Agent
from langchain_ollama import ChatOllama


def get_agent_for(task: str, model: str = 'llama3.2'):
    llm = ChatOllama(model=model)  # 'deepseek-r1'
    return Agent(task=task, llm=llm)
