from typing import List, Optional, Dict, Any
from ..models.graph import Graph, Node, Edge
from ..database.graph_repository import GraphRepository

class GraphService:
    def __init__(self):
        self.repository = GraphRepository()

    def create_graph(
        self,
        name: str,
        description: str,
        nodes: List[Dict[str, Any]],
        edges: List[Dict[str, Any]]
    ) -> Graph:
        """Crée un nouveau graphe"""
        graph = Graph(
            nodes=[Node(**node) for node in nodes],
            edges=[Edge(**edge) for edge in edges]
        )
        return self.repository.save(name, description, graph)

    def get_graph(self, graph_id: str) -> Optional[Graph]:
        """Récupère un graphe par son ID"""
        return self.repository.get(graph_id)

    def list_graphs(self) -> List[Dict[str, Any]]:
        """Liste tous les graphes"""
        return self.repository.list_all()

    def delete_graph(self, graph_id: str) -> bool:
        """Supprime un graphe"""
        return self.repository.delete(graph_id)

    def validate_graph(self, graph: Graph) -> bool:
        """Valide la structure d'un graphe"""
        # Vérifier que tous les edges référencent des nodes existants
        node_ids = {node.id for node in graph.nodes}
        for edge in graph.edges:
            if edge.source not in node_ids or edge.target not in node_ids:
                return False
        return True
