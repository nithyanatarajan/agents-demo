import asyncio

from agno.agent import Agent
from agno.tools.dalle import DalleTools

from config import get_logger
from task_based_agent import agent

logger = get_logger(__name__)


async def run_task(
    task: str = 'Smart-casual for rainy day office',
    provider: str = 'OpenAI',
    model: str = 'gpt-4o',
) -> str:
    try:
        stylist_agent = Agent(
            model=agent.get_model_for(provider, model),
            tools=[DalleTools()],
            description="You're a fashion stylist AI that suggests outfit visuals based on user needs.",
            instructions='Generate a stylish outfit image based on the given description using DALL·E.',
            markdown=True,
            show_tool_calls=True,
        )
        message = f'Getting agent for task: {task}, provider: {provider}, model: {model}'
        logger.info(message)

        result = 'No Image Generated!'
        stylist_agent.print_response(task)

        images = stylist_agent.get_images()
        if images and isinstance(images, list):
            for image_response in images:
                result = image_response.url

        return result
    except Exception as e:
        return f'Error: {e!s}'


async def main():
    await run_task()


if __name__ == '__main__':
    asyncio.run(main())
