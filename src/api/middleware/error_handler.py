from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from typing import Union, Dict, Any

class APIError(Exception):
    def __init__(
        self,
        message: str,
        status_code: int = 400,
        details: Union[Dict[str, Any], None] = None
    ):
        self.message = message
        self.status_code = status_code
        self.details = details or {}
        super().__init__(self.message)

class LLMProviderError(APIError):
    def __init__(self, message: str, provider: str, details: Dict[str, Any] = None):
        super().__init__(
            message=f"LLM Provider Error ({provider}): {message}",
            status_code=503,
            details=details or {}
        )

class ValidationError(APIError):
    def __init__(self, message: str, details: Dict[str, Any] = None):
        super().__init__(
            message=f"Validation Error: {message}",
            status_code=422,
            details=details or {}
        )

async def error_handler(request: Request, exc: Exception) -> JSONResponse:
    """Gestionnaire global des erreurs"""
    if isinstance(exc, APIError):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "error": exc.message,
                "details": exc.details,
                "path": request.url.path
            }
        )
    
    # Erreur non gérée
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "details": str(exc),
            "path": request.url.path
        }
    )

def add_error_handler(app: FastAPI) -> None:
    """Ajoute le gestionnaire d'erreurs à l'application FastAPI"""
    app.add_exception_handler(Exception, error_handler)
    app.add_exception_handler(APIError, error_handler)
    app.add_exception_handler(LLMProviderError, error_handler)
    app.add_exception_handler(ValidationError, error_handler)
