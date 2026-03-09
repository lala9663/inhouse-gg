from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.database import SessionLocal
from models.user import User

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/test-db")
def test_db():

    db: Session = SessionLocal()

    users = db.query(User).all()

    return {"users": users}