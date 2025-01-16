from typing import Dict, List
import uuid
from fastapi import HTTPException
from .base_db_service import BaseDBService

class NodeService(BaseDBService):
    table_name = "nodes"

    @classmethod
    def add_node(cls, graph_id: str, node_data: Dict) -> Dict:
        node_data["_id"] = str(uuid.uuid4())
        node_data["graph_id"] = graph_id
        return cls.create(node_data)

    @classmethod
    def list_nodes(cls, graph_id: str, skip: int = 0, limit: int = 10) -> List[Dict]:
        return cls.list({"graph_id": graph_id}, skip, limit)

    @classmethod
    def get_node(cls, node_id: str) -> Dict:
        node = cls.get_by_id(node_id)
        if not node:
            raise HTTPException(status_code=404, detail={
                "errors": [{
                    "status": "404",
                    "title": "Not Found",
                    "detail": "Node not found"
                }]
            })
        return node

    @classmethod
    def update_node(cls, node_id: str, node_data: Dict) -> Dict:
        node = cls.update(node_id, node_data)
        if not node:
            raise HTTPException(status_code=404, detail={
                "errors": [{
                    "status": "404",
                    "title": "Not Found",
                    "detail": "Node not found"
                }]
            })
        return node

    @classmethod
    def delete_node(cls, node_id: str) -> None:
        if not cls.delete(node_id):
            raise HTTPException(status_code=404, detail={
                "errors": [{
                    "status": "404",
                    "title": "Not Found",
                    "detail": "Node not found"
                }]
            })