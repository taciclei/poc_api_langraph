from typing import Dict, List, Any
from .interface import GraphVisualization
from ..models.graph import Graph, Node, Edge
from ..services.execution_service import ExecutionService
from ..metrics.prometheus import metrics

class D3Visualization(GraphVisualization):
    def __init__(self):
        self.execution_service = ExecutionService()

    async def generate_graph_data(self, graph: Graph) -> Dict[str, Any]:
        """
        Génère les données au format D3.js
        """
        return {
            "nodes": [
                {
                    "id": node.id,
                    "type": node.type,
                    "label": node.label or node.id,
                    "x": node.metadata.get("x", 0),
                    "y": node.metadata.get("y", 0),
                    "data": node.config
                }
                for node in graph.nodes
            ],
            "links": [
                {
                    "source": edge.source,
                    "target": edge.target,
                    "label": edge.label or "",
                    "type": edge.type or "default"
                }
                for edge in graph.edges
            ]
        }

    async def generate_execution_data(self, execution_id: str) -> Dict[str, Any]:
        """
        Génère les données d'exécution en temps réel
        """
        execution = await self.execution_service.get_execution(execution_id)
        if not execution:
            return {}

        return {
            "nodes": [
                {
                    "id": node_id,
                    "status": status,
                    "duration": metrics.llm_latency.labels(
                        provider="execution",
                        cache_hit="false"
                    )._value.get(),
                    "metrics": await self.get_node_metrics(node_id)
                }
                for node_id, status in execution.node_status.items()
            ],
            "timestamp": execution.timestamp,
            "status": execution.status
        }

    async def update_node_position(self, graph_id: str, node_id: str, x: float, y: float) -> bool:
        """
        Met à jour la position d'un nœud dans le graphe
        """
        try:
            # Mettre à jour les métadonnées du nœud
            graph = await self.execution_service.get_graph(graph_id)
            if not graph:
                return False

            for node in graph.nodes:
                if node.id == node_id:
                    if not node.metadata:
                        node.metadata = {}
                    node.metadata["x"] = x
                    node.metadata["y"] = y
                    await self.execution_service.update_graph(graph)
                    return True
            return False
        except Exception:
            return False

    async def get_node_metrics(self, node_id: str) -> Dict[str, Any]:
        """
        Récupère les métriques détaillées d'un nœud
        """
        return {
            "execution_time": metrics.llm_latency.labels(
                provider="node",
                cache_hit="false"
            )._value.get(),
            "memory_usage": 0,  # À implémenter
            "cache_hits": metrics.cache_hits.labels(
                type="node"
            )._value.get(),
            "errors": 0  # À implémenter
        }
