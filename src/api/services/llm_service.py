from typing import Optional, Dict
import os
from dotenv import load_dotenv
from ..llm.model_manager import ModelManager
from ..llm.providers.openai_llm import OpenAILLM
from ..llm.providers.anthropic_llm import AnthropicLLM
from ..llm.providers.palm_llm import PaLMLLM
from ..llm.providers.llama_llm import LlamaLLM
from ..llm.providers.mistral_llm import MistralLLM
from ..llm.providers.deepseek_llm import DeepseekLLM

class LLMService:
    def __init__(self):
        load_dotenv()
        self.model_manager = ModelManager()
        self._configure_providers()

    def _configure_providers(self):
        # OpenAI
        if os.getenv('ENABLE_OPENAI', 'false').lower() == 'true':
            self.model_manager.register_provider(
                'openai',
                OpenAILLM(
                    api_key=os.getenv('OPENAI_API_KEY'),
                    model_name=os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')
                )
            )

        # Anthropic
        if os.getenv('ENABLE_ANTHROPIC', 'false').lower() == 'true':
            self.model_manager.register_provider(
                'anthropic',
                AnthropicLLM(
                    api_key=os.getenv('ANTHROPIC_API_KEY'),
                    model_name=os.getenv('ANTHROPIC_MODEL', 'claude-2')
                )
            )

        # PaLM
        if os.getenv('ENABLE_PALM', 'false').lower() == 'true':
            self.model_manager.register_provider(
                'palm',
                PaLMLLM(
                    api_key=os.getenv('PALM_API_KEY'),
                    model_name=os.getenv('PALM_MODEL')
                )
            )

        # Llama
        if os.getenv('ENABLE_LLAMA', 'false').lower() == 'true':
            self.model_manager.register_provider(
                'llama',
                LlamaLLM(
                    model_path=os.getenv('LLAMA_MODEL_PATH'),
                    n_ctx=int(os.getenv('LLAMA_N_CTX', '2048')),
                    n_threads=int(os.getenv('LLAMA_N_THREADS', '4'))
                )
            )

        # Mistral
        if os.getenv('ENABLE_MISTRAL', 'false').lower() == 'true':
            self.model_manager.register_provider(
                'mistral',
                MistralLLM(
                    api_key=os.getenv('MISTRAL_API_KEY'),
                    model_name=os.getenv('MISTRAL_MODEL', 'mistral-medium')
                )
            )

        # Deepseek
        if os.getenv('ENABLE_DEEPSEEK', 'false').lower() == 'true':
            self.model_manager.register_provider(
                'deepseek',
                DeepseekLLM(
                    api_key=os.getenv('DEEPSEEK_API_KEY'),
                    model_name=os.getenv('DEEPSEEK_MODEL', 'deepseek-chat')
                )
            )

    def get_available_providers(self) -> List[str]:
        return list(self.model_manager.providers.keys())

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
