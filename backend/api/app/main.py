from fastapi import FastAPI

from app.routers import auth, rooms
from app.database import engine

from app.models import user, room
from app.database import engine


user.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="inhouse.gg API",
    description="LoL Inhouse Matchmaking Platform",
    version="0.1.0"
)

app.include_router(auth.router)
app.include_router(rooms.router)

# 테이블 생성
user.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(rooms.router)


@app.get("/")
def root():
    return {"message": "Welcome to inhouse.gg"}