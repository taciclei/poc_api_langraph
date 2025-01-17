from typing import Dict, Any, List
from src.api.config import get_settings

settings = get_settings()

class LLMService:
    def __init__(self):
        self.model = settings.LLM_MODEL
        self.api_key = settings.LLM_API_KEY
        self.temperature = settings.LLM_TEMPERATURE
        self.max_tokens = settings.LLM_MAX_TOKENS

    async def complete(self, prompt: Dict[str, Any]) -> Dict[str, Any]:
        """Génère une complétion de texte"""
        # TODO: Implémenter l'appel à l'API LLM réelle
        return {
            "model": self.model,
            "completion": f"Sample completion for: {prompt.get('text', '')}",
            "tokens_used": 10
        }

    async def chat(self, messages: List[Dict[str, str]]) -> Dict[str, Any]:
        """Génère une réponse de chat"""
        # TODO: Implémenter l'appel à l'API LLM réelle
        return {
            "model": self.model,
            "response": "Sample response",
            "tokens_used": 10
        }
