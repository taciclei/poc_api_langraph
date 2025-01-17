import pytest

@pytest.mark.asyncio
async def test_create_graph(client, test_graph):
    response = await client.post("/api/v1/graphs/", json=test_graph)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == test_graph["name"]

@pytest.mark.asyncio
async def test_get_graph(client, test_graph):
    # Créer d'abord un graphe
    await client.post("/api/v1/graphs/", json=test_graph)
    response = await client.get(f"/api/v1/graphs/{test_graph['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == test_graph["name"]

@pytest.mark.asyncio
async def test_list_graphs(client):
    response = await client.get("/api/v1/graphs/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

@pytest.mark.asyncio
async def test_update_graph(client, test_graph):
    # Créer d'abord un graphe
    await client.post("/api/v1/graphs/", json=test_graph)
    updated_data = {**test_graph, "name": "Updated Graph"}
    response = await client.put(f"/api/v1/graphs/{test_graph['id']}", json=updated_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Graph"

@pytest.mark.asyncio
async def test_delete_graph(client, test_graph):
    # Créer d'abord un graphe
    await client.post("/api/v1/graphs/", json=test_graph)
    response = await client.delete(f"/api/v1/graphs/{test_graph['id']}")
    assert response.status_code == 200
