from fastapi import APIRouter
from src.api.visualization.d3_visualization import D3Visualization

router = APIRouter()

@router.get("/graph/{graph_id}")
async def get_visualization(graph_id: str):
    visualizer = D3Visualization()
    return await visualizer.generate_visualization(graph_id)
