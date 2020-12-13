from typing import Optional, List

from pydantic import Schema

from .db import DateTimeModelMixin, DBModelMixin
from .base import AppBaseModel


class Book(AppBaseModel):
    title: str
    description: Optional[str] = None
    tags: List[str]


class BookFilterParams(AppBaseModel):
    title: str = None
    tags: Optional[List[str]]
    limit: int = 10


class BookInDB(DBModelMixin, Book):
    # url: str
    pass


class BookInResponse(AppBaseModel):
    book: Book


class ManyBooksinResponse(AppBaseModel):
    books: List[Book]
    books_count: int = Schema(..., alias='bookCount')

