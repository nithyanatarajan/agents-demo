from smart_runner.agents import google_agent, gpt_agent, ollama_agent
from smart_runner.config import get_logger

logger = get_logger(__name__)


async def run_browser_task(
    task: str, provider: str = 'OpenAI', model: str = 'gpt-4o'
) -> str:
    try:
        message = (
            f'Getting agent for task: {task}, provider: {provider}, model: {model}'
        )
        logger.info(message)

        if provider == 'OpenAI':
            agent = gpt_agent.get_agent_for(task, model)
        elif provider == 'Google':
            agent = google_agent.get_agent_for(task, model)
        else:
            agent = ollama_agent.get_agent_for(task, model)

        result = await agent.run()
        #  TODO: The result cloud be parsed better
        return result
    except Exception as e:
        return f'Error: {e!s}'
