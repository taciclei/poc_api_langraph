import os
import sys

# Ajouter le répertoire racine au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.api.models import Graph, Node, Edge

# Configuration de la base de données
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def seed_test_data():
    session = SessionLocal()
    try:
        # Créer un graphe de test
        test_graph = Graph(
            name="Test LangChain Flow",
            description="Un graphe de test pour démontrer les capacités de LangChain"
        )
        session.add(test_graph)
        session.flush()  # Pour obtenir l'ID du graphe

        # Créer des nœuds
        llm_node = Node(
            graph_id=test_graph.id,
            name="LLM Node",
            type="llm",
            config={
                "model": "mistral-7b-instruct",
                "temperature": 0.7
            },
            position={"x": 100, "y": 100}
        )

        prompt_node = Node(
            graph_id=test_graph.id,
            name="Prompt Template",
            type="prompt",
            config={
                "template": "Tu es un assistant qui {instruction}."
            },
            position={"x": 300, "y": 100}
        )

        output_node = Node(
            graph_id=test_graph.id,
            name="Output Parser",
            type="output_parser",
            config={
                "format": "json"
            },
            position={"x": 500, "y": 100}
        )

        session.add_all([llm_node, prompt_node, output_node])
        session.flush()

        # Créer des arêtes
        edges = [
            Edge(
                graph_id=test_graph.id,
                source_id=prompt_node.id,
                target_id=llm_node.id,
                config={"type": "prompt"}
            ),
            Edge(
                graph_id=test_graph.id,
                source_id=llm_node.id,
                target_id=output_node.id,
                config={"type": "completion"}
            )
        ]
        session.add_all(edges)

        # Créer un deuxième graphe
        chat_graph = Graph(
            name="Chat Assistant",
            description="Un graphe pour le chat avec mémoire"
        )
        session.add(chat_graph)
        session.flush()

        # Nœuds pour le chat
        memory_node = Node(
            graph_id=chat_graph.id,
            name="Memory",
            type="memory",
            config={
                "type": "buffer",
                "k": 5
            },
            position={"x": 100, "y": 200}
        )

        chat_node = Node(
            graph_id=chat_graph.id,
            name="Chat Model",
            type="chat_model",
            config={
                "model": "mistral-7b-instruct",
                "temperature": 0.8
            },
            position={"x": 300, "y": 200}
        )

        session.add_all([memory_node, chat_node])
        session.flush()

        # Arête pour le chat
        chat_edge = Edge(
            graph_id=chat_graph.id,
            source_id=memory_node.id,
            target_id=chat_node.id,
            config={"type": "context"}
        )
        session.add(chat_edge)

        session.commit()
        print("Données de test insérées avec succès!")

    except Exception as e:
        print(f"Erreur lors de l'insertion des données : {e}")
        session.rollback()
        raise
    finally:
        session.close()

if __name__ == "__main__":
    seed_test_data()
