from fastapi import FastAPI

from app.core.logging import setup_logging
from app.api.v1 import documents, auth

setup_logging()

app = FastAPI()

app.include_router(auth.router)
app.include_router(documents.router, prefix="/api/v1")
