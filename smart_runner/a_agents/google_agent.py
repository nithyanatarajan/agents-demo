import os

from agno.agent import Agent
from agno.models.google import Gemini


def get_agent_with(description: str, model: str = 'gemini-2.0-flash-exp'):
    return Agent(
        model=Gemini(model, api_key=os.getenv('GEMINI_API_KEY')),
        description=description,
        markdown=True,
    )
