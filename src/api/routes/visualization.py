from fastapi import APIRouter, HTTPException
from ..visualization.d3_visualization import D3Visualization
from ..services.graph_service import GraphService

router = APIRouter(prefix="/visualization", tags=["visualization"])
visualizer = D3Visualization()
graph_service = GraphService()

@router.get("/graph/{graph_id}")
async def get_graph_visualization(graph_id: str):
    """Récupère les données de visualisation d'un graphe"""
    graph = await graph_service.get_graph(graph_id)
    if not graph:
        raise HTTPException(status_code=404, detail="Graphe non trouvé")
    return await visualizer.generate_graph_data(graph)

@router.get("/execution/{execution_id}")
async def get_execution_visualization(execution_id: str):
    """Récupère les données de visualisation d'une exécution"""
    return await visualizer.generate_execution_data(execution_id)

@router.put("/graph/{graph_id}/node/{node_id}/position")
async def update_node_position(
    graph_id: str,
    node_id: str,
    x: float,
    y: float
):
    """Met à jour la position d'un nœud"""
    success = await visualizer.update_node_position(graph_id, node_id, x, y)
    if not success:
        raise HTTPException(
            status_code=400,
            detail="Impossible de mettre à jour la position"
        )
    return {"success": True}

@router.get("/node/{node_id}/metrics")
async def get_node_metrics(node_id: str):
    """Récupère les métriques d'un nœud"""
    return await visualizer.get_node_metrics(node_id)
