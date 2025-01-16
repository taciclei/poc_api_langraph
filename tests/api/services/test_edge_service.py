import pytest
from src.api.services.edge_service import EdgeService
from fastapi import HTTPException

def test_create_edge(mocker):
    mocker.patch('src.api.services.edge_service.NodeService.get_node',
                 return_value={"graph_id": "test_graph_id"})
    
    edge_data = {
        "source_id": "source_id",
        "target_id": "target_id",
        "type": "default"
    }
    result = EdgeService.create_edge("test_graph_id", edge_data)
    assert result["source_id"] == edge_data["source_id"]
    assert "_id" in result

def test_validate_nodes_different_graphs(mocker):
    mocker.patch('src.api.services.edge_service.NodeService.get_node',
                 side_effect=[
                     {"graph_id": "graph1"},
                     {"graph_id": "graph2"}
                 ])
    
    with pytest.raises(HTTPException):
        EdgeService.validate_nodes("graph1", "source_id", "target_id")
