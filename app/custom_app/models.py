from dataclasses import dataclass

from dataclass.validators import (
    validate_int,
    validate_str
)

@dataclass
class Search:
    search: str = None

    def __post_init__(self):
        self.search = None if self.search is None else validate_str(self.search, "search")

@dataclass
class Data:
    name: str
    number: int

@dataclass
class Post:
    name: str
    number: int

    def __post_init__(self):
        self.name = validate_str(self.name, "name")
        self.number = validate_int(self.number, "number")
