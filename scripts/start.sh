#!/bin/bash
set -e

# Exécuter les migrations
echo "Running database migrations..."
alembic upgrade head

# Démarrer l'application
echo "Starting application..."
uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --reload
