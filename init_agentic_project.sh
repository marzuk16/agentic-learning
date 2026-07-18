#!/bin/bash

set -e

echo "⚠️ Cleaning repository..."

# Keep git history
find . -mindepth 1 -maxdepth 1 \
  ! -name ".git" \
  ! -name "init_agentic_project.sh" \
  -exec rm -rf {} +

echo "🚀 Creating final Agentic AI src-layout structure..."


# =========================
# Root files
# =========================

touch README.md
touch LICENSE
touch PROJECT_STRUCTURE.md
touch .env.example
touch pyproject.toml
touch Makefile
touch Dockerfile


# =========================
# Docker Compose
# =========================

cat > docker-compose.yml <<'EOF'
services:

  postgres:
    image: pgvector/pgvector:pg16
    container_name: agentic-postgres
    restart: unless-stopped

    environment:
      POSTGRES_DB: agentic_db
      POSTGRES_USER: agentic_user
      POSTGRES_PASSWORD: agentic_password

    ports:
      - "5432:5432"

    volumes:
      - postgres_data:/var/lib/postgresql/data


  redis:
    image: redis:7-alpine
    container_name: agentic-redis
    restart: unless-stopped

    ports:
      - "6379:6379"

    volumes:
      - redis_data:/data


volumes:

  postgres_data:

  redis_data:
EOF


# =========================
# Environment
# =========================

cat > .env.example <<'EOF'
APP_NAME=agentic-learning

POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=agentic_db
POSTGRES_USER=agentic_user
POSTGRES_PASSWORD=agentic_password

REDIS_HOST=localhost
REDIS_PORT=6379

MODEL_PROVIDER=mlx
MODEL_NAME=
EOF


# =========================
# Python Config
# =========================

cat > pyproject.toml <<'EOF'
[project]
name = "agentic-learning"
version = "0.1.0"
description = "Production Agentic AI Engineering Platform"
requires-python = ">=3.12"

dependencies = [
    "fastapi",
    "uvicorn[standard]",
    "langchain",
    "langgraph",
    "sqlalchemy",
    "psycopg[binary]",
    "pgvector",
    "redis",
    "pydantic",
    "pydantic-settings",
    "python-dotenv"
]


[dependency-groups]
dev = [
    "pytest",
    "ruff",
    "mypy"
]


[tool.setuptools.packages.find]
where = ["src"]
EOF


# =========================
# Makefile
# =========================

cat > Makefile <<'EOF'
install:
	uv sync

run:
	uv run uvicorn agentic.api.main:app --reload

test:
	uv run pytest

lint:
	uv run ruff check .
EOF


# =========================
# SRC APPLICATION
# =========================

mkdir -p src/agentic


touch src/agentic/__init__.py


# API
mkdir -p src/agentic/api/routes
mkdir -p src/agentic/api/schemas

touch src/agentic/api/main.py
touch src/agentic/api/routes/chat.py
touch src/agentic/api/routes/health.py


# Agents

for agent in planner researcher coder reviewer k8s
do
    mkdir -p src/agentic/agents/$agent/tests

    touch src/agentic/agents/$agent/__init__.py
    touch src/agentic/agents/$agent/agent.py
    touch src/agentic/agents/$agent/prompts.py
done


# Workflow

mkdir -p src/agentic/workflows/langgraph

touch src/agentic/workflows/langgraph/state.py
touch src/agentic/workflows/langgraph/nodes.py
touch src/agentic/workflows/langgraph/edges.py
touch src/agentic/workflows/langgraph/workflow.py


# RAG

mkdir -p src/agentic/rag/{ingestion,embeddings,retrieval,evaluation}

touch src/agentic/rag/ingestion/loader.py
touch src/agentic/rag/ingestion/chunker.py
touch src/agentic/rag/embeddings/embedding.py
touch src/agentic/rag/retrieval/retriever.py


# MCP

mkdir -p src/agentic/mcp/{servers,clients}

touch src/agentic/mcp/servers/file_server.py
touch src/agentic/mcp/servers/git_server.py
touch src/agentic/mcp/clients/client.py


# Database

mkdir -p src/agentic/database

touch src/agentic/database/postgres.py
touch src/agentic/database/models.py


# LLM

mkdir -p src/agentic/llm

touch src/agentic/llm/client.py
touch src/agentic/llm/prompts.py


# Memory

mkdir -p src/agentic/memory

touch src/agentic/memory/short_term.py
touch src/agentic/memory/long_term.py


# Config

mkdir -p src/agentic/config

touch src/agentic/config/settings.py


# Utils

mkdir -p src/agentic/utils

touch src/agentic/utils/logger.py
touch src/agentic/utils/exceptions.py


# =========================
# Experiments
# =========================

experiments=(
"week01-llm"
"week02-rag"
"week03-repository-chat"
"week04-repository-agent"
"week05-langgraph"
"week06-multi-agent"
"week07-memory"
"week08-mcp"
"week09-reviewer"
"week10-microservice"
"week11-k8s-agent"
)

for exp in "${experiments[@]}"
do
    mkdir -p experiments/$exp
    touch experiments/$exp/README.md
done


# =========================
# Capstone
# =========================

mkdir -p capstone

touch capstone/README.md


# =========================
# Tests
# =========================

mkdir -p tests/{unit,integration,e2e}


# =========================
# Docs
# =========================

mkdir -p docs/{decisions,diagrams}

touch docs/architecture.md
touch docs/roadmap.md


# =========================
# Deployment
# =========================

mkdir -p deployment/{docker,kubernetes}

touch deployment/docker/Dockerfile

touch deployment/kubernetes/deployment.yaml
touch deployment/kubernetes/service.yaml


# =========================
# Scripts
# =========================

mkdir -p scripts

touch scripts/setup.sh
touch scripts/run_local.sh


# =========================
# Notebooks
# =========================

mkdir -p notebooks/experiments


# =========================
# PROJECT STRUCTURE DOC
# =========================

cat > PROJECT_STRUCTURE.md <<'EOF'
# Agentic Learning Project Structure

## src/agentic

Main production application package.

Contains:

- API
- Agents
- Workflows
- RAG
- LLM integration
- Database
- Memory
- MCP


## experiments

Weekly learning experiments.

Contains:

- LLM basics
- RAG experiments
- Repository agents
- Multi-agent examples
- MCP learning


## capstone

Final production-grade Agentic AI application.

Combines all learned concepts.


## tests

Automated testing.

- unit
- integration
- e2e


## docs

Architecture and technical documentation.


## deployment

Deployment configuration.

Contains:

- Docker
- Kubernetes


## scripts

Developer automation scripts.


## notebooks

Research and experimentation notebooks.


## Infrastructure

docker-compose provides:

- PostgreSQL + pgvector
- Redis


## Architecture Philosophy

- Clean Architecture
- Separation of Concerns
- Reusable Components
- Production First
- Test Driven Development
EOF


echo ""
echo "✅ Agentic AI repository initialized successfully!"
echo ""
echo "Next commands:"
echo ""
echo "uv venv"
echo "source .venv/bin/activate"
echo "uv sync"
echo "docker compose up -d"