from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .routes import ai_summary, dashboard, filters

BASE_DIR = Path(__file__).resolve().parent

load_dotenv()

app = FastAPI(title="Car Specs & MPG Dashboard API")

app.include_router(filters.router)
app.include_router(dashboard.router)
app.include_router(ai_summary.router)

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.get("/health")
def health():
    return {"status": "ok"}
