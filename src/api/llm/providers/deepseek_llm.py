from typing import Dict, List, Optional
import requests
from ..interface.base_llm import BaseLLM, LLMResponse

class DeepseekLLM(BaseLLM):
    def __init__(self, api_key: str, model_name: str = "deepseek-chat"):
        self.api_key = api_key
        self.model_name = model_name
        self.api_url = "https://api.deepseek.com/v1/chat/completions"

    async def generate(self, 
                      prompt: str,
                      max_tokens: Optional[int] = None,
                      temperature: float = 0.7,
                      stop_sequences: Optional[List[str]] = None) -> LLMResponse:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": self.model_name,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stop": stop_sequences
        }
        
        response = requests.post(self.api_url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        
        return LLMResponse(
            text=result["choices"][0]["message"]["content"],
            tokens_used=result["usage"]["total_tokens"],
            model_name=self.model_name,
            provider="deepseek",
            metadata={"finish_reason": result["choices"][0]["finish_reason"]}
        )

    async def stream(self, 
                    prompt: str,
                    max_tokens: Optional[int] = None,
                    temperature: float = 0.7,
                    stop_sequences: Optional[List[str]] = None):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": self.model_name,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stop": stop_sequences,
            "stream": True
        }
        
        response = requests.post(self.api_url, headers=headers, json=data, stream=True)
        response.raise_for_status()
        
        for line in response.iter_lines():
            if line:
                chunk = line.decode('utf-8').replace('data: ', '')
                if chunk != '[DONE]':
                    result = json.loads(chunk)
                    if content := result["choices"][0]["delta"].get("content"):
                        yield content

    def get_token_count(self, text: str) -> int:
        # Estimation simple pour Deepseek
        return len(text.split()) * 1.3
