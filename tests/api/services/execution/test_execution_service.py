import pytest
from src.api.services.execution.execution_service import ExecutionService

@pytest.fixture
def execution_service():
    return ExecutionService()

@pytest.fixture
def sample_graph_config():
    return {
        "id": "test-graph",
        "nodes": [
            {
                "id": "node1",
                "type": "llm",
                "config": {
                    "prompt_template": "Summarize: {input}"
                }
            },
            {
                "id": "node2",
                "type": "processing",
                "config": {}
            }
        ],
        "edges": [
            {
                "source": "node1",
                "target": "node2"
            }
        ]
    }

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
async def test_execute_graph(execution_service, sample_graph_config):
    # First, insert the test graph
    execution_service.graphs_db.insert(sample_graph_config)
    
    result = await execution_service.execute_graph(
        "test-graph",
        {"input": "This is a test input"}
    )
    assert result["status"] == "completed"
    assert "execution_id" in result
    assert "result" in result

@pytest.mark.asyncio
async def test_get_execution_status(execution_service):
    execution_id = await execution_service.create_execution(
        "test-graph-id",
        {"input": "test"}
    )
    status = await execution_service.get_execution_status(execution_id)
    assert "status" in status
    assert "input_data" in status

@pytest.mark.asyncio
async def test_list_executions(execution_service):
    await execution_service.create_execution(
        "test-graph-id",
        {"input": "test1"}
    )
    await execution_service.create_execution(
        "test-graph-id",
        {"input": "test2"}
    )
    executions = await execution_service.list_executions("test-graph-id")
    assert len(executions) >= 2
