from typing import Optional, List

from fastapi import APIRouter, Depends, Query

from ..crud.utils import create_aliased_response
from ..crud.book import get_books_with_filters
from ..db.mongodb import AsyncIOMotorClient, get_database
from ..models.book import BookFilterParams, BookInResponse, ManyBooksinResponse


router = APIRouter()


@router.get('/search', tags=['search'])
async def search_books(
    filters: BookFilterParams,
    db: AsyncIOMotorClient = Depends(get_database)
):
    dbbooks = await get_books_with_filters(
        db, filters
    )
    return create_aliased_response(
        ManyBooksinResponse(books=dbbooks, books_count=len(dbbooks))
    )


