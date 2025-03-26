from fastapi import FastAPI
from app.api import register_routers
from app.config import settings

app = FastAPI(title="Taskmanagr", version="1.0")

register_routers(app)

@app.get("/")
async def root():
    return {"message": "Hello World"}