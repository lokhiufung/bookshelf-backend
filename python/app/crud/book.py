from typing import List, Optional
from bson import ObjectId

from ..models.book import BookFilterParams, BookInDB, Book
from ..db.mongodb import AsyncIOMotorClient

from ..config import DATABASE_NAME, BOOK_COLLECTION


async def get_books_with_filters(
    conn: AsyncIOMotorClient, filters: BookFilterParams
) -> List[BookInDB]:
    
    books: List[BookInDB] = []

    query = {}
    if filters.title:
        # search book with an EXACT title
        title = filters.title
        query['title'] = { '$in': title }
    elif filters.tags:
        tags = filters.tags
        query['tags'] = { '$in': tags}

    rows = conn[DATABASE_NAME][BOOK_COLLECTION].find(query, limit=filters.limit)
    
    async for row in rows:
        books.append(
            BookInDB(
                **row,
                createdAt=ObjectId(row['_id']).generation_time,
                updatedAt=ObjectId(row['_id']).generation_time
            )
        )
    return books


async def create_books(
    conn: AsyncIOMotorClient, books: List[Book]
) -> List[BookInDB]:

    insert_result = await conn[DATABASE_NAME][BOOK_COLLECTION].insert_many([book.dict() for book in books])
    created_ids = insert_result.inserted_ids
    return created_ids


async def delete_books(
    conn: AsyncIOMotorClient, ids: List[ObjectId]
) -> List[BookInDB]:
    query = {}
    query['_id'] = {'$in': ids}
    deleted = await conn[DATABASE_NAME][BOOK_COLLECTION].delete_many(query)
    return deleted.deleted_count

