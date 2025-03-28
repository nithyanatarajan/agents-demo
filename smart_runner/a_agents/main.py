import asyncio
import sys

from smart_runner.a_agents.ollama_agent import get_agent_with
from smart_runner.config import get_logger

logger = get_logger(__name__)


async def main():
    task_from_cli = ' '.join(sys.argv[1:]).strip()
    logger.debug(f'Task from CLI: {task_from_cli}')
    task = 'Tell me about a breaking news story from New York.'
    task = task_from_cli if len(task_from_cli) > 1 else task
    logger.debug(f'Task given to agent: {task_from_cli}')
    description = 'You are an enthusiastic news reporter with a flair for storytelling!'
    agent = get_agent_with(description)
    agent.print_response(task, stream=True)


if __name__ == '__main__':
    asyncio.run(main())
