def test_create_graph(client):
    response = client.post(
        "/graphs/",
        json={
            "name": "test_graph",
            "description": "Test graph"
        }
    )
    assert response.status_code == 200
    assert response.json()["name"] == "test_graph"

def test_get_graph(client):
    # First create a graph
    graph_id = client.post(
        "/graphs/",
        json={
            "name": "test_graph",
            "description": "Test graph"
        }
    ).json()["id"]
    
    # Then get it
    response = client.get(f"/graphs/{graph_id}")
    assert response.status_code == 200
    assert response.json()["id"] == graph_id

def test_list_graphs(client):
    response = client.get("/graphs/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_delete_graph(client):
    # First create a graph
    graph_id = client.post(
        "/graphs/",
        json={
            "name": "test_graph",
            "description": "Test graph"
        }
    ).json()["id"]
    
    # Then delete it
    response = client.delete(f"/graphs/{graph_id}")
    assert response.status_code == 200
    
    # Verify it's gone
    response = client.get(f"/graphs/{graph_id}")
    assert response.status_code == 404
