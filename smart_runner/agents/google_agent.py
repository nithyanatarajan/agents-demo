import os

from browser_use import Agent
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr

load_dotenv()


def get_agent_for(task: str, model: str = 'gemini-2.0-flash-exp'):
    llm = ChatGoogleGenerativeAI(model=model, api_key=SecretStr(os.getenv('GEMINI_API_KEY')))

    return Agent(task=task, llm=llm)
