from typing import Optional, Dict
from ..llm.model_manager import ModelManager
from ..llm.providers.openai_llm import OpenAILLM
from ..llm.providers.anthropic_llm import AnthropicLLM
from ..llm.providers.palm_llm import PaLMLLM
from ..llm.providers.llama_llm import LlamaLLM

class LLMService:
    def __init__(self, config: Dict[str, str]):
        self.model_manager = ModelManager()
        
        # Configuration des providers
        if 'OPENAI_API_KEY' in config:
            self.model_manager.register_provider(
                'openai',
                OpenAILLM(api_key=config['OPENAI_API_KEY'])
            )
        
        if 'ANTHROPIC_API_KEY' in config:
            self.model_manager.register_provider(
                'anthropic',
                AnthropicLLM(api_key=config['ANTHROPIC_API_KEY'])
            )
        
        if 'PALM_API_KEY' in config:
            self.model_manager.register_provider(
                'palm',
                PaLMLLM(api_key=config['PALM_API_KEY'])
            )
        
        if 'LLAMA_MODEL_PATH' in config:
            self.model_manager.register_provider(
                'llama',
                LlamaLLM(model_path=config['LLAMA_MODEL_PATH'])
            )

    async def generate(self,
                      prompt: str,
                      provider: Optional[str] = None,
                      use_cache: bool = True,
                      **kwargs):
        return await self.model_manager.generate(
            prompt=prompt,
            provider_name=provider,
            use_cache=use_cache,
            **kwargs
        )

    async def stream(self,
                    prompt: str,
                    provider: Optional[str] = None,
                    **kwargs):
        async for chunk in self.model_manager.stream(
            prompt=prompt,
            provider_name=provider,
            **kwargs
        ):
            yield chunk
