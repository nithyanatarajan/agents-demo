from browser_use import Agent
from langchain_ollama import ChatOllama


def get_agent_for(task: str, model: str = 'qwen2.5'):
    llm = ChatOllama(model=model, num_ctx=32000)
    return Agent(task=task, llm=llm)
