import asyncio
import pprint

from motor.motor_asyncio import AsyncIOMotorClient

from app.crud.book import get_books_with_filters, create_books, delete_books
from app.models.book import BookFilterParams, Book


conn = AsyncIOMotorClient()


async def test_get_books_with_filters():
    filters = BookFilterParams(titles='<seeder>')
    result = await get_books_with_filters(conn, filters)
    pprint.pprint(result)


async def test_create_books():
    books = [
        Book(title='test book', tags=['test', 'test2']),
        Book(title='test book 2', tags=['test2', 'test2222']),
    ]
    result = await create_books(conn, books)
    pprint.pprint(result)


loop = asyncio.get_event_loop()
loop.run_until_complete(test_get_books_with_filters())
loop.run_until_complete(test_create_books())

