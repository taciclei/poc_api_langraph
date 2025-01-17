import pytest
from src.api.llm.fallback.llm_manager import LLMManager
from src.api.llm.providers.openai_llm import OpenAILLM
from src.api.llm.providers.anthropic_llm import AnthropicLLM

@pytest.fixture
def llm_manager():
    providers = [
        OpenAILLM(model_name="gpt-3.5-turbo"),
        AnthropicLLM(model_name="claude-2")
    ]
    return LLMManager(providers=providers)

@pytest.mark.asyncio
async def test_generate_with_fallback(llm_manager):
    response = await llm_manager.generate_with_fallback(
        prompt="Test prompt",
        max_tokens=100
    )
    assert response.text
    assert response.tokens_used > 0
    assert response.provider in ["openai", "anthropic"]

@pytest.mark.asyncio
async def test_stream_with_fallback(llm_manager):
    chunks = []
    async for chunk in llm_manager.stream_with_fallback(
        prompt="Test prompt",
        max_tokens=100
    ):
        chunks.append(chunk)
    assert len(chunks) > 0
