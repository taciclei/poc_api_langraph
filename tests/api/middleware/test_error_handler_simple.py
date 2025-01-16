import pytest
from fastapi import status
from src.api.middleware.error_handler import APIError

def test_api_error_creation_simple():
    error = APIError(
        message="Test error",
        status_code=status.HTTP_400_BAD_REQUEST,
        details={"field": "test"}
    )
    assert error.message == "Test error"
    assert error.status_code == status.HTTP_400_BAD_REQUEST
    assert error.details == {"field": "test"}
