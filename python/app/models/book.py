# from bson import ObjectId
from typing import Optional, List

from pydantic import Schema

from .db import DateTimeModelMixin, DBModelMixin
from .base import AppBaseModel


class BookBase(AppBaseModel):
    title: str
    tags: List[str]
    url: str
    description: Optional[str]


class BookInServer(BookBase):
    book_id: Optional[str]


class BookFilterParams(AppBaseModel):
    title: str = None
    tags: Optional[List[str]]
    book_id: Optional[str]
    limit: int = 10


class BookInDB(DBModelMixin, BookInServer):
    """Book retrieved from DB"""
    pass


class ManyBookCreateResposnse(AppBaseModel):
    # created_ids: List[str] = Schema(..., alias='createdIds')
    # created_count: int = Schema(..., alias='createdCount')
    # created_ids: List[str]
    created_count: int


class ManyBookDeleteResponse(AppBaseModel):
    # deleted_ids: List[str] = Schema(..., alias='deletedIds')
    # deleted_count: int = Schema(..., alias='deletedCount')
    deleted_count: int


class ManyBookUpdateResponse(AppBaseModel):
    # deleted_ids: List[str] = Schema(..., alias='deletedIds')
    # updated_count: int = Schema(..., alias='updatedCount')
    updated_count: int

# class BookSearchResponse(AppBaseModel):
#     book: Book
    

class ManyBookSearchResponse(AppBaseModel):
    books: List[BookInDB]
    books_count: int = Schema(..., alias='bookCount')

