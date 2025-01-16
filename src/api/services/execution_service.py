from typing import Dict, List, Optional
import uuid
from fastapi import HTTPException
from langgraph.graph import Graph
from .base_db_service import BaseDBService
from .node_service import NodeService
from .edge_service import EdgeService

class ExecutionService(BaseDBService):
    table_name = "executions"

    @classmethod
    def execute_graph(cls, graph_id: str, inputs: Dict) -> Dict:
        # Récupérer les nœuds et les arêtes
        nodes = NodeService.list_nodes(graph_id)
        edges = EdgeService.list_edges(graph_id)

        # Créer une instance de Graph LangGraph
        graph = Graph()
        
        # Ajouter les nœuds et les arêtes
        for node in nodes:
            graph.add_node(node["_id"], **node)
        
        for edge in edges:
            graph.add_edge(
                edge["source_id"],
                edge["target_id"],
                condition=edge.get("condition")
            )

        # Exécuter le graphe
        execution_data = {
            "_id": str(uuid.uuid4()),
            "graph_id": graph_id,
            "inputs": inputs
        }

        try:
            result = graph.execute(inputs)
            execution_data.update({
                "status": "completed",
                "result": result,
                "metadata": {}
            })
        except Exception as e:
            execution_data.update({
                "status": "failed",
                "result": {"error": str(e)},
                "metadata": {"error_type": type(e).__name__}
            })

        return cls.create(execution_data)

    @classmethod
    def get_execution(cls, execution_id: str) -> Dict:
        execution = cls.get_by_id(execution_id)
        if not execution:
            raise HTTPException(status_code=404, detail={
                "errors": [{
                    "status": "404",
                    "title": "Not Found",
                    "detail": "Execution not found"
                }]
            })
        return execution

    @classmethod
    def list_executions(cls, graph_id: str, status: Optional[str] = None, skip: int = 0, limit: int = 10) -> List[Dict]:
        filter_dict = {"graph_id": graph_id}
        if status:
            filter_dict["status"] = status
        return cls.list(filter_dict, skip, limit)