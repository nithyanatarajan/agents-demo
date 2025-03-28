from agno.agent import Agent
from agno.models.openai import OpenAIChat


def get_agent_with(description: str, model: str = 'gpt-4o-mini'):
    return Agent(model=(OpenAIChat(id=model)), description=description, markdown=True)
