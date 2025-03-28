from agno.models.openai import OpenAIChat


def get_model(model: str = 'gpt-4o-mini'):
    return OpenAIChat(id=model)
