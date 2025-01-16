from src.api.routes import execution_routes
app.include_router(execution_routes.router)
from src.api.routes import execution_routes
app.include_router(execution_routes.router)

# Add error handling
from src.api.middleware.error_handler import APIError, error_handler
from src.api.middleware.logging_middleware import LoggingMiddleware

app.add_middleware(LoggingMiddleware)
app.add_exception_handler(APIError, error_handler)
