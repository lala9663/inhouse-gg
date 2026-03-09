from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base


class Room(Base):

    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    host_id = Column(Integer, ForeignKey("users.id"))
    status = Column(String, default="waiting")