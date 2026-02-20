from fastapi import FastAPI
from app.api.v1 import documents, auth

app = FastAPI()

app.include_router(documents.router, prefix="/api/v1")
app.include_router(auth.router)
