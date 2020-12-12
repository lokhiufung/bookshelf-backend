from typing import List, Optional
from bson import ObjectId

from ..models.book import BookFilterParams, BookInDB
from ..db.mongodb import AsyncIOMotorClient

from ..config import DATABASE_NAME, BOOK_COLLECTION


async def get_books_with_filters(
    conn: AsyncIOMotorClient, filters: BookFilterParams
) -> List[BookInDB]:
    
    books: List[BookInDB] = []

    if filters.title:
        # search book with an EXACT title
        pass
    elif filters.tags:
        rows = conn[DATABASE_NAME][BOOK_COLLECTION]
    
    async for row in rows:
        books.append(
            BookInDB(
                **row,
                created_at=ObjectId(row['_id']).generation_time,
            )
        )