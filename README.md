# API LangGraph

API de gestion de graphes pour le traitement du langage naturel avec support multi-LLMs.

## 🌟 Fonctionnalités

- Support multi-providers LLM (OpenAI, Mistral, Hugging Face)
- Gestion complète des graphes (CRUD)
- Validation avancée des graphes
- Système d'exécution avec monitoring
- Cache intelligent (en cours)
- API RESTful documentée

## 🚀 Installation

\```bash
# Cloner le repository
git clone https://github.com/yourusername/poc_api_langraph.git
cd poc_api_langraph

# Installer les dépendances
pip install -r requirements.txt

# Configurer les variables d'environnement
cp .env.template .env
# Éditer .env avec vos clés API
\```

## 📖 Documentation

### Configuration des LLMs

Pour utiliser les différents LLMs, configurez vos clés API dans le fichier `.env` :

\```bash
# OpenAI
ENABLE_OPENAI=true
OPENAI_API_KEY=your_key_here
OPENAI_MODEL=gpt-4

# Mistral
ENABLE_MISTRAL=true
MISTRAL_API_KEY=your_key_here
MISTRAL_MODEL=mistral-medium

# Hugging Face
ENABLE_HUGGINGFACE=true
HUGGINGFACE_API_KEY=your_key_here
HUGGINGFACE_MODEL=mistralai/Mistral-7B-Instruct-v0.2
\```

### Utilisation de l'API

#### Lister les providers LLM disponibles

\```bash
curl -X GET http://localhost:8000/llm/providers
\```

#### Générer du texte avec un LLM spécifique

\```bash
curl -X POST http://localhost:8000/llm/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Votre prompt ici", "provider": "mistral"}'
\```

#### Créer un nouveau graphe

\```bash
curl -X POST http://localhost:8000/graphs \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Mon Graphe",
    "description": "Description du graphe",
    "nodes": [],
    "edges": []
  }'
\```

## 🔄 Versions

- [x] Version 0.1.0 : Structure de base
- [x] Version 0.2.0 : Gestion des graphes
- [x] Version 0.3.0 : Système d'exécution
- [x] Version 1.0.0 : Support multi-LLMs
- [ ] Version 1.1.0 : Cache et monitoring avancé

## 📊 Roadmap

Voir [ROADMAP.md](ROADMAP.md) pour les détails des futures versions.

## 🛠 Stack Technique

- Python 3.12+
- FastAPI
- SQLite
- TinyDB

## 📝 License

MIT License

## Nouvelles fonctionnalités (v1.1.0)

### Gestion des graphes
\`\`\`python
# Exemple de création d'un graphe
graph = Graph(name="Mon Graphe", description="Description du graphe")

# Ajout de nœuds
node1 = Node(
    graph_id=graph.id,
    name="Node 1",
    type="llm",
    config={"model": "mistral-7b-instruct"}
)

# Création de relations
edge = Edge(
    graph_id=graph.id,
    source_id=node1.id,
    target_id=node2.id,
    config={"type": "data_flow"}
)
\`\`\`

### Migrations
\`\`\`bash
# Créer une nouvelle migration
make migrations message="ma_migration"

# Appliquer les migrations
make migrate

# Revenir en arrière
make rollback
\`\`\`

### Tests
\`\`\`bash
# Exécuter les tests
make test

# Insérer des données de test
python scripts/seed_test_data.py
\`\`\`
