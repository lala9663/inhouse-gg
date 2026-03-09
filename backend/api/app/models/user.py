from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    puuid = Column(String, unique=True, index=True)
    game_name = Column(String)
    tag_line = Column(String)
    tier = Column(String)
    rank = Column(String)