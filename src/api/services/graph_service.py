from typing import Dict, List, Optional
from datetime import datetime
from uuid import uuid4

from src.api.models.graph import Graph, GraphCreate, GraphUpdate
from src.api.repositories.graph_repository import GraphRepository

class GraphService:
    def __init__(self):
        self.repository = GraphRepository()

    async def create_graph(self, graph_data: GraphCreate) -> Graph:
        """Crée un nouveau graphe"""
        graph = Graph(
            id=str(uuid4()),
            name=graph_data.name,
            description=graph_data.description,
            nodes=graph_data.nodes,
            edges=graph_data.edges,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        return await self.repository.create(graph)

    async def get_graph(self, graph_id: str) -> Optional[Graph]:
        """Récupère un graphe par son ID"""
        return await self.repository.get(graph_id)

    async def update_graph(self, graph_id: str, graph_data: GraphUpdate) -> Optional[Graph]:
        """Met à jour un graphe existant"""
        existing_graph = await self.repository.get(graph_id)
        if not existing_graph:
            return None

        updated_data = graph_data.model_dump(exclude_unset=True)
        updated_data["updated_at"] = datetime.utcnow()

        return await self.repository.update(graph_id, updated_data)

    async def delete_graph(self, graph_id: str) -> bool:
        """Supprime un graphe"""
        return await self.repository.delete(graph_id)

    async def list_graphs(self, skip: int = 0, limit: int = 10) -> List[Graph]:
        """Liste tous les graphes avec pagination"""
        return await self.repository.list(skip=skip, limit=limit)
