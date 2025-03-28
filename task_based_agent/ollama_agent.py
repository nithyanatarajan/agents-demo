from agno.models.ollama import Ollama


def get_model(model: str = 'qwen2.5'):
    return Ollama(id=model)
