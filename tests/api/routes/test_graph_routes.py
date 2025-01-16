import pytest
from httpx import AsyncClient
import pytest_asyncio
from src.api.main import app

@pytest_asyncio.fixture
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

@pytest.fixture
def sample_graph_request():
    return {
        "name": "Test Graph",
        "description": "Test Description",
        "nodes": ["node1", "node2"],
        "edges": [{"source": "node1", "target": "node2"}]
    }

@pytest.mark.asyncio
async def test_create_graph(async_client, sample_graph_request):
    """Test graph creation"""
    response = await async_client.post("/graph/create", json=sample_graph_request)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["name"] == sample_graph_request["name"]

@pytest.mark.asyncio
async def test_get_graph(async_client):
    """Test graph retrieval"""
    # First create a graph
    response = await async_client.post("/graph/create", json={
        "name": "Test Graph",
        "description": "Test Description",
        "nodes": ["node1"],
        "edges": []
    })
    graph_id = response.json()["id"]
    
    # Then get it
    response = await async_client.get(f"/graph/get/{graph_id}")
    assert response.status_code == 200
    assert response.json()["id"] == graph_id

@pytest.mark.asyncio
async def test_get_nonexistent_graph(async_client):
    """Test getting a non-existent graph"""
    response = await async_client.get("/graph/get/nonexistent")
    assert response.status_code == 404
    assert "Graph not found" in response.json()["message"]

@pytest.mark.asyncio
async def test_delete_graph(async_client):
    """Test graph deletion"""
    # First create a graph
    response = await async_client.post("/graph/create", json={
        "name": "Test Graph",
        "description": "Test Description",
        "nodes": ["node1"],
        "edges": []
    })
    graph_id = response.json()["id"]
    
    # Then delete it
    response = await async_client.delete(f"/graph/delete/{graph_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Graph deleted successfully"
    
    # Verify it's gone
    response = await async_client.get(f"/graph/get/{graph_id}")
    assert response.status_code == 404
