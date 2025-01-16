import pytest
from fastapi import Request, Response
from src.api.middleware.logging_middleware import LoggingMiddleware

@pytest.mark.asyncio
async def test_logging_middleware():
    """Test logging middleware"""
    middleware = LoggingMiddleware(app=None)
    
    # Mock request
    class MockURL:
        path = "/test"
    
    class MockRequest:
        url = MockURL()
        method = "GET"
    
    # Mock call_next
    async def mock_call_next(request):
        return Response(status_code=200)
    
    # Test middleware
    response = await middleware.dispatch(MockRequest(), mock_call_next)
    assert response.status_code == 200

