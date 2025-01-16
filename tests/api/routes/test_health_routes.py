import pytest
from fastapi.testclient import TestClient
from src.api.main import app

@pytest.fixture(scope="module")
def test_app():
    from fastapi import FastAPI
    return app

@pytest.fixture(scope="module")
def test_client(test_app):
    from fastapi.testclient import TestClient
    with TestClient(test_app) as client:
        yield client

def test_health_check(test_client):
    """Test health check endpoint"""
    response = test_client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
