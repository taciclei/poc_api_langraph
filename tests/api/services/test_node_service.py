import pytest
from src.api.services.node_service import NodeService

def test_create_node():
    node_data = {
        "name": "Test Node",
        "type": "process",
        "graph_id": "test_graph_id"
    }
    result = NodeService.create_node(node_data["graph_id"], node_data)
    assert result["name"] == node_data["name"]
    assert "_id" in result

def test_list_nodes():
    graph_id = "test_graph_id"
    nodes = NodeService.list_nodes(graph_id)
    assert isinstance(nodes, list)
