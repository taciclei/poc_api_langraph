import time
import logging
import uuid
from typing import Callable
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

# Configuration du logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("api")

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        request_id = str(uuid.uuid4())
        start_time = time.time()
        
        # Log de début de requête
        logger.info(
            f"Request started | ID: {request_id} | "
            f"Method: {request.method} | "
            f"Path: {request.url.path}"
        )

        # Traitement de la requête
        try:
            response = await call_next(request)
            process_time = time.time() - start_time
            
            # Log de fin de requête
            logger.info(
                f"Request completed | ID: {request_id} | "
                f"Status: {response.status_code} | "
                f"Duration: {process_time:.3f}s"
            )
            
            # Ajout des headers de traçage
            response.headers["X-Request-ID"] = request_id
            response.headers["X-Process-Time"] = str(process_time)
            
            return response
            
        except Exception as e:
            process_time = time.time() - start_time
            logger.error(
                f"Request failed | ID: {request_id} | "
                f"Error: {str(e)} | "
                f"Duration: {process_time:.3f}s"
            )
            raise

def add_logging_middleware(app: FastAPI) -> None:
    """Ajoute le middleware de logging à l'application FastAPI"""
    app.add_middleware(LoggingMiddleware)
