from fastapi import FastAPI

app = FastAPI(
    title="inhouse.gg API",
    description="LoL Inhouse Matchmaking Platform",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to inhouse.gg API"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }