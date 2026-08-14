from fastapi import FastAPI

from .routes import filters

app = FastAPI(title="Car Specs & MPG Dashboard API")

app.include_router(filters.router)


@app.get("/")
def root():
    return {"status": "ok"}
