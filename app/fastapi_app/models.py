from pydantic import BaseModel

class Data(BaseModel):
    name: str
    number: int

class Post(BaseModel):
    name: str
    number: int
