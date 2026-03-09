from fastapi import APIRouter

router = APIRouter(prefix="/rooms", tags=["rooms"])

@router.get("/")
def get_rooms():
    return {"rooms": []}