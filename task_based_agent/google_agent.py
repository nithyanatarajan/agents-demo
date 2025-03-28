import os

from agno.models.google import Gemini


def get_model(model: str = 'gemini-2.0-flash-exp'):
    return Gemini(id=model, api_key=os.getenv('GEMINI_API_KEY'))
