from abc import ABC, abstractmethod
from typing import Dict, List, Any
from ..models.graph import Graph, Node, Edge

class GraphVisualization(ABC):
    @abstractmethod
    async def generate_graph_data(self, graph: Graph) -> Dict[str, Any]:
        """Génère les données de visualisation pour un graphe"""
        pass

    @abstractmethod
    async def generate_execution_data(self, execution_id: str) -> Dict[str, Any]:
        """Génère les données de visualisation pour une exécution"""
        pass

    @abstractmethod
    async def update_node_position(self, graph_id: str, node_id: str, x: float, y: float) -> bool:
        """Met à jour la position d'un nœud"""
        pass

    @abstractmethod
    async def get_node_metrics(self, node_id: str) -> Dict[str, Any]:
        """Récupère les métriques d'un nœud"""
        pass
