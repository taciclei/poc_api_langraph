from typing import Dict, List, Optional
import uuid
from fastapi import HTTPException
from .base_db_service import BaseDBService
from .node_service import NodeService

class EdgeService(BaseDBService):
    table_name = "edges"

    @classmethod
    def validate_nodes(cls, graph_id: str, source_id: str, target_id: str):
        source = NodeService.get_node(source_id)
        target = NodeService.get_node(target_id)
        
        if source["graph_id"] != graph_id or target["graph_id"] != graph_id:
            raise HTTPException(
                status_code=400,
                detail="Source and target nodes must belong to the same graph"
            )

    @classmethod
    def create_edge(cls, graph_id: str, edge_data: Dict) -> Dict:
        cls.validate_nodes(graph_id, edge_data["source_id"], edge_data["target_id"])
        edge_data["_id"] = str(uuid.uuid4())
        edge_data["graph_id"] = graph_id
        return cls.create(edge_data)

    @classmethod
    def list_edges(cls, graph_id: str) -> List[Dict]:
        return cls.list({"graph_id": graph_id})
