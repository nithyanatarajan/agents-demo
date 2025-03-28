from config import get_logger
from task_based_agent import google_agent, gpt_agent, ollama_agent

logger = get_logger(__name__)


def get_model_for(provider: str = 'OpenAI', model: str = 'gpt-4o'):
    message = f'Getting agent for provider: {provider}, model: {model}'
    logger.info(message)

    if provider == 'OpenAI':
        model = gpt_agent.get_model(model)
    elif provider == 'Google':
        model = google_agent.get_model(model)
    else:
        model = ollama_agent.get_model(model)

    return model
