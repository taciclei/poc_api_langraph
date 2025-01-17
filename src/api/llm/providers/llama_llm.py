from typing import Dict, List, Optional
from llama_cpp import Llama
from ..interface.base_llm import BaseLLM, LLMResponse

class LlamaLLM(BaseLLM):
    def __init__(self, model_path: str, n_ctx: int = 2048, n_threads: int = 4):
        self.model = Llama(
            model_path=model_path,
            n_ctx=n_ctx,
            n_threads=n_threads
        )
        self.model_name = "llama2"

    async def generate(self, 
                      prompt: str,
                      max_tokens: Optional[int] = None,
                      temperature: float = 0.7,
                      stop_sequences: Optional[List[str]] = None) -> LLMResponse:
        response = self.model(
            prompt,
            max_tokens=max_tokens or 2048,
            temperature=temperature,
            stop=stop_sequences
        )
        
        return LLMResponse(
            text=response['choices'][0]['text'],
            tokens_used=response['usage']['total_tokens'],
            model_name=self.model_name,
            provider="llama",
            metadata={"finish_reason": response['choices'][0]['finish_reason']}
        )

    async def stream(self, 
                    prompt: str,
                    max_tokens: Optional[int] = None,
                    temperature: float = 0.7,
                    stop_sequences: Optional[List[str]] = None):
        stream = self.model(
            prompt,
            max_tokens=max_tokens or 2048,
            temperature=temperature,
            stop=stop_sequences,
            stream=True
        )
        for chunk in stream:
            if chunk['choices'][0]['text']:
                yield chunk['choices'][0]['text']

    def get_token_count(self, text: str) -> int:
        return len(self.model.tokenize(text.encode()))
