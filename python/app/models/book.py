from typing import Optional, List

from pydantic import BaseConfig, BaseModel


class Book(BaseModel):
    title: str
    description: Optional[str] = None
    tags: List[str]


class BookFilterParams(BaseModel):
    title: str
    tags: List[str]
    limit: int = 10


class BookInDB(BaseModel):
    pass

