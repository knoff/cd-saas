from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .api import health

app = FastAPI(title="CD SaaS API")
app.include_router(health.router, prefix="/health", tags=["health"])

# /static/web/* → файлы из app/static/web (vite build)
app.mount("/static", StaticFiles(directory="app/static", html=False), name="static")
