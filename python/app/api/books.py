from typing import Optional, List

from fastapi import APIRouter, Depends, Query

from ..crud.utils import create_aliased_response
from ..crud import book as book_crud 
from ..db.mongodb import AsyncIOMotorClient, get_database
from ..models.book import (
    BookFilterParams, BookBase,
    ManyBookSearchResponse, ManyBookCreateResposnse,
    ManyBookDeleteResponse, ManyBookUpdateResponse
)


router = APIRouter()


@router.post('/', tags=['book-crud', 'search'])
async def search_books_by_filters(
    filters: BookFilterParams,
    db: AsyncIOMotorClient = Depends(get_database)
):
    dbbooks = await book_crud.get_books_by_filters(
        db, filters
    )
    return create_aliased_response(
        ManyBookSearchResponse(books=dbbooks, bookCount=len(dbbooks))
    )


@router.post('/bulk', tags=['book-crud'])
async def create_books(
    books: List[BookBase],
    db: AsyncIOMotorClient = Depends(get_database)
):
    created = await book_crud.create_books(
        db, books
    )
    return create_aliased_response(
        ManyBookCreateResposnse(**created)
    )


@router.delete('/', tags=['book-crud'])
async def delete_book(
    filters: BookFilterParams,
    db: AsyncIOMotorClient = Depends(get_database),
):
    deleted = await book_crud.delete_book_by_filters(db, filters)
    return create_aliased_response(
        ManyBookDeleteResponse(**deleted)
    )


@router.put('/', tags=['book-crud'])
async def udpate_book(
    filters: BookFilterParams,
    book: BookBase,
    db: AsyncIOMotorClient = Depends(get_database),
):
    updated = await book_crud.update_book_by_filters(db, filters, book)
    return create_aliased_response(
        ManyBookUpdateResponse(**updated)
    )
    
    
