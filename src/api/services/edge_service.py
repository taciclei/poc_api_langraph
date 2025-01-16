from typing import Dict, List
import uuid
from fastapi import HTTPException
from .base_db_service import BaseDBService

class EdgeService(BaseDBService):
    table_name = "edges"

    @classmethod
    def add_edge(cls, graph_id: str, edge_data: Dict) -> Dict:
        edge_data["_id"] = str(uuid.uuid4())
        edge_data["graph_id"] = graph_id
        return cls.create(edge_data)

    @classmethod
    def list_edges(cls, graph_id: str, skip: int = 0, limit: int = 10) -> List[Dict]:
        return cls.list({"graph_id": graph_id}, skip, limit)

    @classmethod
    def get_edge(cls, edge_id: str) -> Dict:
        edge = cls.get_by_id(edge_id)
        if not edge:
            raise HTTPException(status_code=404, detail={
                "errors": [{
                    "status": "404",
                    "title": "Not Found",
                    "detail": "Edge not found"
                }]
            })
        return edge

    @classmethod
    def update_edge(cls, edge_id: str, edge_data: Dict) -> Dict:
        edge = cls.update(edge_id, edge_data)
        if not edge:
            raise HTTPException(status_code=404, detail={
                "errors": [{
                    "status": "404",
                    "title": "Not Found",
                    "detail": "Edge not found"
                }]
            })
        return edge

    @classmethod
    def delete_edge(cls, edge_id: str) -> None:
        if not cls.delete(edge_id):
            raise HTTPException(status_code=404, detail={
                "errors": [{
                    "status": "404",
                    "title": "Not Found",
                    "detail": "Edge not found"
                }]
            })