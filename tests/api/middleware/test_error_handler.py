import pytest
from fastapi import status, Request
from fastapi.responses import JSONResponse
from src.api.middleware.error_handler import APIError, error_handler

def test_api_error_creation():
    """Test basic error creation"""
    error = APIError(
        message="Test error",
        status_code=status.HTTP_400_BAD_REQUEST,
        details={"field": "test"}
    )
    assert error.message == "Test error"
    assert error.status_code == status.HTTP_400_BAD_REQUEST
    assert error.details == {"field": "test"}

@pytest.mark.asyncio
async def test_error_handler():
    """Test error handler response"""
    # Create mock request
    class MockURL:
        path = "/test"
    
    class MockRequest:
        url = MockURL()
        method = "GET"
    
    error = APIError(
        message="Test error",
        status_code=status.HTTP_400_BAD_REQUEST,
        details={"field": "test"}
    )
    
    response = await error_handler(MockRequest(), error)
    assert isinstance(response, JSONResponse)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    content = response.body.decode()
    assert "Test error" in content
    assert "test" in content
