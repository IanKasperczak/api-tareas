from fastapi import FastAPI
from app.database import engine
from app import models
from app.routers import tasks, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Tareas",
    description="API REST para gestión de tareas personales",
    version="1.0.0"
)

app.include_router(tasks.router)
app.include_router(auth.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}