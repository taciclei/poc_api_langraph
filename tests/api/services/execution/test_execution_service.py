import pytest
from src.api.services.execution.execution_service import ExecutionService

@pytest.fixture
def execution_service():
    return ExecutionService()

@pytest.mark.asyncio
async def test_create_execution(execution_service):
    execution_id = await execution_service.create_execution(
        "test-graph-id",
        {"input": "test"}
    )
    assert execution_id is not None
    status = await execution_service.get_execution_status(execution_id)
    assert status["status"] == "pending"

@pytest.mark.asyncio
async def test_execute_graph(execution_service):
    result = await execution_service.execute_graph(
        "test-graph-id",
        {"input": "test"}
    )
    assert result["status"] == "completed"
    assert "execution_id" in result
