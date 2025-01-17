import pytest
from fastapi.testclient import TestClient
from src.api.main import app

@pytest.fixture
def client():
    """Fixture pour créer un client de test"""
    return TestClient(app)

def test_health_check(client):
    """Test du endpoint de health check"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_metrics_endpoint(client):
    """Test du endpoint de métriques"""
    response = client.get("/metrics")
    assert response.status_code == 200
    data = response.json()
    assert "http_metrics" in data
    assert "llm_metrics" in data

def test_llm_completion(client):
    """Test du endpoint de completion LLM"""
    payload = {
        "prompt": "Hello, how are you?",
        "max_tokens": 50
    }
    response = client.post("/v1/completions", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "text" in data
    assert isinstance(data["text"], str)

def test_llm_stream(client):
    """Test du endpoint de streaming LLM"""
    payload = {
        "prompt": "Count to 5.",
        "max_tokens": 50,
        "stream": True
    }
    response = client.post("/v1/completions", json=payload)
    assert response.status_code == 200
    
    # Vérification du streaming
    content = b''
    for chunk in response.iter_content(chunk_size=None):
        content += chunk
    assert len(content) > 0

def test_invalid_request(client):
    """Test de gestion des erreurs"""
    payload = {
        "prompt": "",  # prompt vide invalide
        "max_tokens": -1  # valeur invalide
    }
    response = client.post("/v1/completions", json=payload)
    assert response.status_code == 422  # Validation error

def test_cache_hit(client):
    """Test du cache"""
    payload = {"prompt": "What is 2+2?"}
    
    # Première requête
    response1 = client.post("/v1/completions", json=payload)
    assert response1.status_code == 200
    
    # Deuxième requête (devrait venir du cache)
    response2 = client.post("/v1/completions", json=payload)
    assert response2.status_code == 200
    assert "X-Cache-Hit" in response2.headers
    assert response2.headers["X-Cache-Hit"] == "true"
