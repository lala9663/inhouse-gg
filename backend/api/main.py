from fastapi import FastAPI
from routers import auth, rooms

app = FastAPI(
    title="inhouse.gg API",
    description="LoL Inhouse Matchmaking Platform",
    version="0.1.0"
)

app.include_router(auth.router)
app.include_router(rooms.router)


@app.get("/")
def root():
    return {"message": "Welcome to inhouse.gg"}