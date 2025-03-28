from agno.agent import Agent
from agno.models.ollama import Ollama


def get_agent_with(description: str, model: str = 'qwen2.5'):
    return Agent(model=(Ollama(id=model)), description=description, markdown=True)
