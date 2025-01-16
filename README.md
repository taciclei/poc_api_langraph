# 🚀 LangGraph API

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/python-3.12-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![LangChain](https://img.shields.io/badge/🦜_LangChain-blue?style=for-the-badge)](https://github.com/hwchase17/langchain)

Une API FastAPI pour créer et exécuter des graphes de traitement de langage naturel avec LangGraph et LangChain.

## 📑 Table des Matières

- [Architecture](#-architecture)
- [Fonctionnalités](#-fonctionnalités)
- [Types de Nœuds](#-types-de-nœuds)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Documentation API](#-documentation-api)
- [Tests](#-tests)
- [Exemples](#-exemples)
- [License](#-license)

## 🏗 Architecture

\`\`\`mermaid
graph TB
    A[Client] -->|HTTP Request| B[FastAPI]
    B --> C[Router Layer]
    C --> D[Service Layer]
    D --> E[Graph Engine]
    E --> F[Node Types]
    F -->|LLM| G[OpenAI]
    F -->|Processing| H[Custom Logic]
    F -->|Validation| I[Schema Check]
    E --> J[TinyDB]
    style A fill:#f9f,stroke:#333,stroke-width:4px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style E fill:#bfb,stroke:#333,stroke-width:2px
\`\`\`

## 🚀 Fonctionnalités

- ⚡️ **Exécution Asynchrone**: Traitement parallèle des nœuds du graphe
- 🔄 **État Persistant**: Sauvegarde automatique de l'état d'exécution
- 🎯 **Validation Intégrée**: Vérification des données à chaque étape
- 📊 **Monitoring**: Suivi en temps réel des exécutions
- 🔌 **Extensible**: Architecture modulaire pour ajouter de nouveaux types de nœuds

## 📋 Types de Nœuds

### Architecture des Nœuds

\`\`\`mermaid
classDiagram
    BaseNode <|-- LLMNode
    BaseNode <|-- ProcessingNode
    BaseNode <|-- ValidationNode
    BaseNode <|-- TransformationNode
    BaseNode <|-- AggregationNode
    BaseNode <|-- FilterNode
    
    class BaseNode{
        +__call__(state) Dict
    }
    class LLMNode{
        +prompt_template
        +memory
        +llm
    }
    class ProcessingNode{
        +processor_func
    }
    class ValidationNode{
        +schema
    }
\`\`\`

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

## 🔧 Installation

### Prérequis

- Python 3.12+
- pip
- git

\`\`\`bash
# Cloner le repository
git clone https://github.com/votre-username/langgraph-api.git
cd langgraph-api

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
.\venv\Scripts\activate  # Windows

# Installer les dépendances
pip install -r requirements.txt

# Configurer les variables d'environnement
cp .env.example .env
# Éditer .env avec vos clés API
\`\`\`

## 🚦 Utilisation

### Flux de Travail Typique

\`\`\`mermaid
sequenceDiagram
    participant C as Client
    participant A as API
    participant G as Graph Engine
    participant N as Nodes
    participant DB as Database
    
    C->>A: Créer un graphe
    A->>DB: Sauvegarder config
    DB-->>A: Confirmer
    A-->>C: graph_id
    
    C->>A: Démarrer exécution
    A->>G: Initialiser graphe
    G->>N: Exécuter nœuds
    N-->>G: Résultats
    G->>DB: Sauvegarder résultats
    G-->>A: Status
    A-->>C: execution_id
\`\`\`

### Exemples d'Utilisation

#### 1. Créer un Graphe de Résumé
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

#### 2. Exécuter le Graphe
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

### Structure du Projet

\`\`\`
src/
├── api/
│   ├── models/          # Modèles Pydantic
│   ├── routes/          # Routes FastAPI
│   ├── services/        # Logique métier
│   │   └── execution/   # Moteur d'exécution
│   └── main.py         # Point d'entrée
├── tests/              # Tests unitaires et d'intégration
└── docs/              # Documentation détaillée
\`\`\`

## 🧪 Tests

\`\`\`bash
# Exécuter tous les tests
pytest tests/ -v

# Exécuter les tests avec couverture
pytest tests/ -v --cov=src

# Exécuter un test spécifique
pytest tests/api/services/test_execution_service.py -v
\`\`\`

## 📝 License

MIT License

## 🤝 Contribution

Les contributions sont les bienvenues ! Consultez notre [guide de contribution](CONTRIBUTING.md).

---

⭐️ Si ce projet vous aide, n'hésitez pas à lui donner une étoile sur GitHub !
