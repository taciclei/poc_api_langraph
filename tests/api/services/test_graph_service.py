import pytest
from src.api.services.graph_service import GraphService

def test_create_graph():
    graph_data = {
        "name": "Test Graph",
        "description": "Test Description"
    }
    result = GraphService.create_graph(graph_data)
    assert result["name"] == graph_data["name"]
    assert "_id" in result

def test_get_graph():
    graph_data = {
        "name": "Test Graph",
        "description": "Test Description"
    }
    created = GraphService.create_graph(graph_data)
    result = GraphService.get_graph(created["_id"])
    assert result["name"] == graph_data["name"]
