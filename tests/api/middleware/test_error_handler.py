import pytest
from fastapi import status
from src.api.middleware.error_handler import APIError, error_handler
from fastapi.testclient import TestClient

async def test_api_error_creation():
    error = APIError(
        message="Test error",
        status_code=status.HTTP_400_BAD_REQUEST,
        details={"field": "test"}
    )
    assert error.message == "Test error"
    assert error.status_code == status.HTTP_400_BAD_REQUEST
    assert error.details == {"field": "test"}

async def test_error_handler_response(test_client: TestClient):
    error = APIError(
        message="Test error",
        status_code=status.HTTP_400_BAD_REQUEST,
        details={"field": "test"}
    )
    request = type('Request', (), {'url': type('URL', (), {'path': '/test'}), 'method': 'GET'})()
    response = await error_handler(request, error)
    
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "error" in response.body.decode()
