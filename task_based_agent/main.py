import asyncio
import sys

from agno.agent import Agent

from config import get_logger
from task_based_agent.ollama_agent import get_model

logger = get_logger(__name__)


async def main():
    task_from_cli = ' '.join(sys.argv[1:]).strip()
    logger.info(f'Task from CLI: {task_from_cli}')
    task = 'Tell me about a breaking news story from New York.'
    task = task_from_cli if len(task_from_cli) > 1 else task
    logger.info(f'Task given to agent: {task}')
    description = 'You are an enthusiastic news reporter with a flair for storytelling!'
    agent = Agent(model=(get_model()), description=description, markdown=True)

    agent.print_response(task, stream=True)


if __name__ == '__main__':
    asyncio.run(main())
