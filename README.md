# POC API LangGraph

Une API RESTful pour gérer des graphes LangChain avec FastAPI et TinyDB.

## Installation

```bash
# Cloner le dépôt
git clone https://github.com/taciclei/poc_api_langraph.git
cd poc_api_langraph

# Installer les dépendances
magic install
```

## Démarrage

```bash
magic run start
```

L'API sera disponible à l'adresse http://localhost:8000

## Documentation

La documentation de l'API est disponible à l'adresse http://localhost:8000/docs

## Structure du projet

```
src/
  ├── api/
  │   ├── models/      # Modèles Pydantic
  │   ├── routes/      # Routes FastAPI
  │   └── services/    # Services métier
  ├── core/           # Configuration et utilitaires
  └── main.py        # Point d'entrée de l'application
```
