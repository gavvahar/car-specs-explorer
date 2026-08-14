from fastapi import FastAPI

app = FastAPI(title="Car Specs & MPG Dashboard API")


@app.get("/")
def root():
    return {"status": "ok"}
