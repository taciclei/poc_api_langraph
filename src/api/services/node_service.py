from typing import Dict, List, Optional
import uuid
from fastapi import HTTPException
from .base_db_service import BaseDBService

class NodeService(BaseDBService):
    table_name = "nodes"

    @classmethod
    def create_node(cls, graph_id: str, node_data: Dict) -> Dict:
        node_data["_id"] = str(uuid.uuid4())
        node_data["graph_id"] = graph_id
        return cls.create(node_data)

    @classmethod
    def get_node(cls, node_id: str) -> Dict:
        node = cls.get_by_id(node_id)
        if not node:
            raise HTTPException(status_code=404, detail="Node not found")
        return node

    @classmethod
    def list_nodes(cls, graph_id: str) -> List[Dict]:
        return cls.list({"graph_id": graph_id})
