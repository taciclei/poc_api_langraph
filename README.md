# 🚀 POC API LangGraph

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/python-3.12-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](CONTRIBUTING.md)

Une API RESTful moderne pour la gestion et l'exécution de graphes LangChain, construite avec FastAPI et TinyDB.

## ✨ Fonctionnalités

- 🌐 API RESTful complète
- 📊 Gestion des graphes LangChain
- 🔄 Exécution de workflows
- 📝 Documentation OpenAPI/Swagger
- 🔒 Gestion des erreurs robuste
- 🚀 Performance optimisée

## 🛠️ Installation

### Prérequis

- Python 3.12+
- Magic CLI

### Installation rapide

```bash
# Cloner le dépôt
git clone https://github.com/taciclei/poc_api_langraph.git
cd poc_api_langraph

# Installer les dépendances
magic install
```

### Variables d'environnement

Copiez le fichier \`.env.example\` vers \`.env\` et ajustez les variables :

```bash
cp .env.example .env
```

## 🚀 Démarrage

```bash
magic run start
```

L'API sera disponible à :
- API : http://localhost:8000
- Documentation : http://localhost:8000/docs
- Documentation alternative : http://localhost:8000/redoc

## 📖 Documentation

La documentation complète est disponible dans le dossier [docs](./docs).

### Points d'entrée principaux

- \`POST /api/v1/graphs\` - Créer un nouveau graphe
- \`GET /api/v1/graphs\` - Lister les graphes
- \`POST /api/v1/graphs/{graph_id}/execute\` - Exécuter un graphe

## 🏗️ Structure du projet

```
src/
  ├── api/            # Composants API
  │   ├── models/     # Modèles Pydantic
  │   ├── routes/     # Routes FastAPI
  │   └── services/   # Services métier
  ├── core/           # Configuration et utilitaires
  └── main.py         # Point d'entrée
```

## 🧪 Tests

```bash
# Exécuter les tests
magic test

# Avec couverture
magic test --cov
```

## 🤝 Contribution

Les contributions sont les bienvenues ! Consultez notre [guide de contribution](CONTRIBUTING.md).

## 📝 License

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 📫 Contact

- Créé par [Taciclei](https://github.com/taciclei)
- Twitter : [@taciclei](https://twitter.com/taciclei)

## 🙏 Remerciements

- [FastAPI](https://fastapi.tiangolo.com/)
- [LangChain](https://python.langchain.com/)
- [TinyDB](https://tinydb.readthedocs.io/)

---

⭐️ Si ce projet vous aide, n'hésitez pas à lui donner une étoile sur GitHub !
