from fastapi import APIRouter, HTTPException, status
from ..services.graph_service import GraphService
from ..schemas.graph_schemas import GraphResponse, GraphRequest
from ..middleware.error_handler import APIError

router = APIRouter(prefix="/graph", tags=["graph"])
graph_service = GraphService()

@router.post("/create", response_model=GraphResponse)
async def create_graph(request: GraphRequest):
    try:
        result = await graph_service.create_graph(request.dict())
        return GraphResponse(**result)
    except Exception as e:
        raise APIError(
            message="Failed to create graph",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            details={"error": str(e)}
        )

@router.get("/get/{graph_id}", response_model=GraphResponse)
async def get_graph(graph_id: str):
    try:
        result = await graph_service.get_graph(graph_id)
        if not result:
            raise APIError(
                message="Graph not found",
                status_code=status.HTTP_404_NOT_FOUND,
                details={"graph_id": graph_id}
            )
        return GraphResponse(**result)
    except APIError:
        raise
    except Exception as e:
        raise APIError(
            message="Failed to retrieve graph",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            details={"error": str(e), "graph_id": graph_id}
        )

@router.delete("/delete/{graph_id}")
async def delete_graph(graph_id: str):
    try:
        result = await graph_service.delete_graph(graph_id)
        if not result:
            raise APIError(
                message="Graph not found",
                status_code=status.HTTP_404_NOT_FOUND,
                details={"graph_id": graph_id}
            )
        return {"message": "Graph deleted successfully", "graph_id": graph_id}
    except APIError:
        raise
    except Exception as e:
        raise APIError(
            message="Failed to delete graph",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            details={"error": str(e), "graph_id": graph_id}
        )
