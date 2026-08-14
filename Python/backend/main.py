from fastapi import FastAPI

from .routes import ai_summary, dashboard, filters

app = FastAPI(title="Car Specs & MPG Dashboard API")

app.include_router(filters.router)
app.include_router(dashboard.router)
app.include_router(ai_summary.router)


@app.get("/")
def root():
    return {"status": "ok"}
