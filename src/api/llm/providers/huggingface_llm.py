from typing import Optional, AsyncGenerator, Dict
from huggingface_hub import InferenceClient
from ..interface.base_llm import BaseLLM, LLMResponse

class HuggingFaceLLM(BaseLLM):
    def __init__(self, api_key: str, model_name: str = "mistralai/Mistral-7B-Instruct-v0.2"):
        self.client = InferenceClient(token=api_key)
        self.model_name = model_name

    async def generate(self, prompt: str, **kwargs) -> LLMResponse:
        response = self.client.text_generation(
            prompt,
            model=self.model_name,
            **kwargs
        )
        return LLMResponse(
            text=response,
            model=self.model_name
        )

    async def stream(self, prompt: str, **kwargs) -> AsyncGenerator[str, None]:
        response = self.client.text_generation(
            prompt,
            model=self.model_name,
            stream=True,
            **kwargs
        )
        for chunk in response:
            yield chunk
