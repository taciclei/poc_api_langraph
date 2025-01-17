import pytest

@pytest.mark.asyncio
async def test_create_node(client, test_graph):
    # Créer d'abord un graphe
    await client.post("/api/v1/graphs/", json=test_graph)
    
    node_data = {
        "name": "Test Node",
        "type": "test",
        "graph_id": test_graph["id"]
    }
    response = await client.post("/api/v1/nodes/", json=node_data)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == node_data["name"]

@pytest.mark.asyncio
async def test_get_node(client, test_graph):
    # Créer d'abord un graphe et un nœud
    await client.post("/api/v1/graphs/", json=test_graph)
    node_data = {
        "name": "Test Node",
        "type": "test",
        "graph_id": test_graph["id"]
    }
    create_response = await client.post("/api/v1/nodes/", json=node_data)
    node_id = create_response.json()["id"]
    
    response = await client.get(f"/api/v1/nodes/{node_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == node_data["name"]
