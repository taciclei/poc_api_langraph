import pytest
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def test_graph():
    return {
        "name": "Test Graph",
        "description": "A test graph",
        "status": "draft"
    }

@pytest.fixture
def test_node():
    return {
        "name": "Test Node",
        "type": "process",
        "config": {"key": "value"}
    }

@pytest.fixture
def test_edge():
    return {
        "source_id": "source_id",
        "target_id": "target_id",
        "type": "default"
    }
