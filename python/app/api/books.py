from typing import Optional, List

from fastapi import APIRouter, Depends, Query
from ..db.mongodb import AsyncIOMotorClient, get_database
from ..models.book import BookFilterParams


router = APIRouter()


@router.get('/search')
async def search_books(
    title: str = "",
    tags: Optional[List[str]] = None,
    limit: int = Query(10, gt=0),
    db: AsyncIOMotorClient = Depends(get_database)
):
    filters = BookFilterParams(
        title=title, tags=tags, limit=limit
    )
    book = await get_books_with_filters(
        db, filters
    )
    return create_aliased_response(
        
    )