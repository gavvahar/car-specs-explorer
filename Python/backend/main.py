from fastapi import FastAPI

from .routes import dashboard, filters

app = FastAPI(title="Car Specs & MPG Dashboard API")

app.include_router(filters.router)
app.include_router(dashboard.router)


@app.get("/")
def root():
    return {"status": "ok"}
