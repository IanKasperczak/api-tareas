from fastapi import FastAPI

app = FastAPI(
    title="API de Tareas",
    description="API REST para gestión de tareas personales",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}