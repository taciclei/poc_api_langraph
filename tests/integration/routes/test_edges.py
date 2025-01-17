import pytest

@pytest.mark.asyncio
async def test_create_edge(client, test_graph):
    # Créer d'abord un graphe et deux nœuds
    await client.post("/api/v1/graphs/", json=test_graph)
    
    node1_data = {
        "name": "Node 1",
        "type": "test",
        "graph_id": test_graph["id"]
    }
    node2_data = {
        "name": "Node 2",
        "type": "test",
        "graph_id": test_graph["id"]
    }
    
    node1_response = await client.post("/api/v1/nodes/", json=node1_data)
    node2_response = await client.post("/api/v1/nodes/", json=node2_data)
    
    edge_data = {
        "source_id": node1_response.json()["id"],
        "target_id": node2_response.json()["id"],
        "graph_id": test_graph["id"]
    }
    
    response = await client.post("/api/v1/edges/", json=edge_data)
    assert response.status_code == 201
    data = response.json()
    assert data["source_id"] == edge_data["source_id"]
