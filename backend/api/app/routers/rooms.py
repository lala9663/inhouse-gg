from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.room import Room

router = APIRouter(prefix="/rooms", tags=["rooms"])


@router.get("/")
def get_rooms():

    db: Session = SessionLocal()

    rooms = db.query(Room).all()

    return rooms

@router.post("/")
def create_room(name: str, host_id: int):

    db: Session = SessionLocal()

    try:
        room = Room(
            name=name,
            host_id=host_id
        )

        db.add(room)
        db.commit()
        db.refresh(room)

        return room

    finally:
        db.close()