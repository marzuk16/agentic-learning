from fastapi import APIRouter

from src.api.routes import documents, search, chat


api_router = APIRouter()


api_router.include_router(documents.router)
api_router.include_router(search.router)
api_router.include_router(chat.router)