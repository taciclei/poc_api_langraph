import pytest
import httpx
from src.api.main import app

@pytest.fixture
async def client():
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app),
        base_url="http://test"
    ) as client:
        yield client

@pytest.fixture
def test_graph():
    return {
        "id": "test-graph",
        "name": "Test Graph",
        "description": "A test graph"
    }

# Configure pytest pour utiliser asyncio
def pytest_configure(config):
    pytest.register_assert_rewrite("tests")
