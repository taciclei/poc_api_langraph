# LangGraph API

Une API FastAPI pour créer et exécuter des graphes de traitement de langage naturel avec LangGraph et LangChain.

## 🚀 Fonctionnalités

- Création et gestion de graphes de traitement
- Exécution asynchrone des workflows
- Multiples types de nœuds spécialisés
- Suivi des exécutions
- API RESTful complète

## 📋 Types de Nœuds Disponibles

### 1. LLMNode
Nœud pour les opérations de modèle de langage
\`\`\`python
{
    "type": "llm",
    "config": {
        "prompt_template": "Résume le texte suivant: {input}",
        "memory": true  # Optional
    }
}
\`\`\`

### 2. ProcessingNode
Nœud pour le traitement personnalisé des données
\`\`\`python
{
    "type": "processing",
    "config": {
        "function": "custom_process"
    }
}
\`\`\`

### 3. ValidationNode
Nœud pour la validation des données
\`\`\`python
{
    "type": "validation",
    "config": {
        "schema": {
            "text": str,
            "count": int
        }
    }
}
\`\`\`

### 4. TransformationNode
Nœud pour la transformation des données
\`\`\`python
{
    "type": "transformation",
    "config": {
        "transformations": {
            "text": "to_upper",
            "data": "to_json"
        }
    }
}
\`\`\`

### 5. AggregationNode
Nœud pour combiner plusieurs entrées
\`\`\`python
{
    "type": "aggregation",
    "config": {
        "custom_aggregation": false  # Optional
    }
}
\`\`\`

### 6. FilterNode
Nœud pour filtrer les données
\`\`\`python
{
    "type": "filter",
    "config": {
        "conditions": {
            "score": "lambda x: x > 0.5"
        }
    }
}
\`\`\`

## 🔧 Installation

\`\`\`bash
# Cloner le repository
git clone https://github.com/votre-username/langgraph-api.git

# Installer les dépendances
pip install -r requirements.txt

# Configurer les variables d'environnement
cp .env.example .env
# Éditer .env avec vos clés API
\`\`\`

## 🚦 Utilisation

### Démarrer l'API
\`\`\`bash
uvicorn src.api.main:app --reload
\`\`\`

### Créer un Graphe
\`\`\`bash
curl -X POST http://localhost:8000/graph/create \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Summarization Workflow",
    "description": "Summarize and process text",
    "nodes": [
      {
        "id": "summarize",
        "type": "llm",
        "config": {
          "prompt_template": "Summarize: {input}"
        }
      },
      {
        "id": "validate",
        "type": "validation",
        "config": {
          "schema": {
            "text": "str"
          }
        }
      }
    ],
    "edges": [
      {
        "source": "summarize",
        "target": "validate"
      }
    ]
  }'
\`\`\`

### Exécuter un Graphe
\`\`\`bash
curl -X POST http://localhost:8000/execution/start \
  -H "Content-Type: application/json" \
  -d '{
    "graph_id": "votre-graph-id",
    "input_data": {
      "input": "Votre texte à traiter"
    }
  }'
\`\`\`

## 📚 Documentation API

La documentation Swagger est disponible à l'adresse : \`http://localhost:8000/docs\`

## 🧪 Tests

\`\`\`bash
# Exécuter les tests
pytest tests/ -v
\`\`\`

## 📝 License

MIT License
