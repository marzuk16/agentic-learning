install:
	uv sync

run:
	uv run uvicorn agentic.api.main:app --reload

test:
	uv run pytest

lint:
	uv run ruff check .
