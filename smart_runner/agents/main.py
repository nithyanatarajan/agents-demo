import asyncio

from ollama_agent import get_agent_for


async def main():
    # task = 'Compare the price of gpt-4o and DeepSeek-V3'
    task = 'Open amazon.in and add a product to cart'
    agent = get_agent_for(task)
    result = await agent.run()
    print(result)  # noqa: T201


if __name__ == '__main__':
    asyncio.run(main())
