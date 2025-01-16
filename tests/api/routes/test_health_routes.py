from fastapi.testclient import TestClient
from src.api.main import app

def test_health_check():
    """Test health check endpoint"""
    with TestClient(app) as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "healthy"}
