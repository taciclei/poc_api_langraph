import pytest
from fastapi.testclient import TestClient

@pytest.fixture
def test_client():
    from src.api.main import app
    return TestClient(app)
