import asyncio
import pprint

from motor.motor_asyncio import AsyncIOMotorClient

from app.crud.book import (
    get_books_by_filters, create_books,
    delete_book_by_filters, update_book_by_filters
)
from app.models.book import BookFilterParams, BookBase, BookInServer


conn = AsyncIOMotorClient()


async def test_get_books_by_filters():
    filters = BookFilterParams(title='test book')
    # print(filters)
    result = await get_books_by_filters(conn, filters)
    pprint.pprint(result)


async def test_create_books():
    books = [
        BookBase(title='test book', tags=['test', 'test2'], url='http://xxx.com'),
        BookBase(title='test book 2', tags=['test2', 'test2222'], url='http://yyy.com'),
    ]
    result = await create_books(conn, books)
    pprint.pprint(result)


# async def test_delete_books_by_ids():/
async def test_update_books_by_filters():
    filters = BookFilterParams(title='test book')
    update_book = BookInServer(title='test book', url='http://zzz.com', tags=['str'])
    result = await update_book_by_filters(conn, filters, update_book)
    pprint.pprint(result)


async def test_delete_books_by_filters():
    filters = BookFilterParams(title='test book 2')
    result = await delete_book_by_filters(conn, filters=filters)
    pprint.pprint(result)



loop = asyncio.get_event_loop()
# loop.run_until_complete(test_get_books_by_filters())
loop.run_until_complete(test_create_books())
# loop.run_until_complete(test_update_books_by_filters())
# loop.run_until_complete(test_delete_books_by_filters())


