from fastapi import APIRouter

from app.database import SessionLocal

router = APIRouter(prefix="/rooms", tags=["rooms"])

@router.get("/")
def get_rooms():
    return {"rooms": []}