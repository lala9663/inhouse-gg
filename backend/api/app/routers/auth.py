from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.user import User

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def get_users():

    db: Session = SessionLocal()

    try:
        users = db.query(User).all()
        return users

    finally:
        db.close()
    
@router.post("/")
def create_user(
    puuid: str,
    game_name: str,
    tag_line: str,
    tier: str = None,
    rank: str = None
):

    db: Session = SessionLocal()

    try:
        user = User(
            puuid=puuid,
            game_name=game_name,
            tag_line=tag_line,
            tier=tier,
            rank=rank
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    finally:
        db.close()

@router.get("/{user_id}")
def get_user(user_id: int):

    db: Session = SessionLocal()

    try:
        user = db.query(User).filter(User.id == user_id).first()
        return user

    finally:
        db.close()