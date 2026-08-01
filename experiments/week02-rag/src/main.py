from fastapi import FastAPI

from src.app.lifespan import lifespan
from src.app.router import api_router


app = FastAPI(
    title="Agentic AI Platform",
    lifespan=lifespan,
)


app.include_router(
    api_router
)