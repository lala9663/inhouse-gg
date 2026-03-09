from pydantic import BaseModel

class UserCreate(BaseModel):
    puuid: str
    game_name: str
    tag_line: str


class UserResponse(BaseModel):
    id: int
    puuid: str
    game_name: str
    tag_line: str

    class Config:
        from_attributes = True