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

@pytest.fixture
def sample_graph_request():
    return {
        "name": "Test Graph",
        "description": "Test Description",
        "nodes": ["node1", "node2"],
        "edges": [{"source": "node1", "target": "node2"}]
    }

def test_create_graph(test_client, sample_graph_request):
    """Test graph creation"""
    response = test_client.post("/graph/create", json=sample_graph_request)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["name"] == sample_graph_request["name"]

def test_get_graph(test_client):
    """Test graph retrieval"""
    # First create a graph
    response = test_client.post("/graph/create", json={
        "name": "Test Graph",
        "description": "Test Description",
        "nodes": ["node1"],
        "edges": []
    })
    graph_id = response.json()["id"]
    
    # Then get it
    response = test_client.get(f"/graph/get/{graph_id}")
    assert response.status_code == 200
    assert response.json()["id"] == graph_id

def test_get_nonexistent_graph(test_client):
    """Test getting a non-existent graph"""
    response = test_client.get("/graph/get/nonexistent")
    assert response.status_code == 404
    assert "Graph not found" in response.json()["message"]

def test_delete_graph(test_client):
    """Test graph deletion"""
    # First create a graph
    response = test_client.post("/graph/create", json={
        "name": "Test Graph",
        "description": "Test Description",
        "nodes": ["node1"],
        "edges": []
    })
    graph_id = response.json()["id"]
    
    # Then delete it
    response = test_client.delete(f"/graph/delete/{graph_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Graph deleted successfully"
    
    # Verify it's gone
    response = test_client.get(f"/graph/get/{graph_id}")
    assert response.status_code == 404
