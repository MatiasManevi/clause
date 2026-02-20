from fastapi import FastAPI
from app.routers import documents, auth

app = FastAPI()

app.include_router(documents.router)
app.include_router(auth.router)
