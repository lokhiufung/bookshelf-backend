from typing import List, Optional
from bson import ObjectId

from ..models.book import BookFilterParams, BookInDB, BookInServer, BookBase
from ..db.mongodb import AsyncIOMotorClient

from ..config import DATABASE_NAME, BOOK_COLLECTION

# __all__ = ['get_books_by_filters', 'create_books', 'delete_books_by_ids']


async def get_books_by_filters(
    conn: AsyncIOMotorClient, filters: BookFilterParams
) -> List[BookInDB]:
    
    books: List[BookInDB] = []

    query = {}
    if filters.title:
        # search book with an EXACT title
        query['title'] = filters.title 
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
    conn: AsyncIOMotorClient, books: List[BookBase]
) -> dict:
    books_ = []
    for book_base in books:
        books_.append(BookInServer(
            **book_base.dict(),
            book_id = str(ObjectId())
        ))
    insert_result = await conn[DATABASE_NAME][BOOK_COLLECTION].insert_many([book.dict() for book in books_])
    created_ids = [id_ for id_ in insert_result.inserted_ids]
    return {
        'created_ids': created_ids,
        'created_count': len(created_ids)
    }


async def delete_book_by_filters(
    conn: AsyncIOMotorClient, filters: BookFilterParams
) -> dict:
    query = {}
    if filters.title:
        query['title'] = filters.title
    elif filters.book_id:
        query['book_id'] = filters.book_id
    
    deleted = await conn[DATABASE_NAME][BOOK_COLLECTION].delete_one(query)
    deleted_count = deleted.deleted_count 
    return {
        'deleted_count': deleted_count
    }


async def update_book_by_filters(
    conn: AsyncIOMotorClient, filters: BookFilterParams, book: BookInServer
) -> dict:
    query = {}
    if filters.title:
        query['title'] = filters.title
    elif filters.book_id:
        query['book_id'] = filters.book_id
    
    update_dict = {k: v for k, v in book.dict().items() if v}
    updated = await conn[DATABASE_NAME][BOOK_COLLECTION].update_one(
        query, {
            '$set': update_dict
        })
    return {
        'updated_count': updated.modified_count
    }