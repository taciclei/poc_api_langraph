from setuptools import setup, find_packages

setup(
    name="poc_api_langraph",
    version="1.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.100.0",
        "uvicorn>=0.22.0",
        "sqlalchemy>=2.0.0",
        "alembic>=1.14.0",
        "psycopg2-binary>=2.9.9",
        "asyncpg>=0.30.0",
    ],
)
