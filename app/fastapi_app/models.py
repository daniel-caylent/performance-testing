from pydantic import BaseModel, Extra

class CustomBaseModel(BaseModel):
    class Config:
        """Forbid extra parameters."""
        extra = Extra.forbid

class Search(CustomBaseModel):
    search: str = None

class Data(CustomBaseModel):
    name: str
    number: int

class Post(CustomBaseModel):
    name: str
    number: int
