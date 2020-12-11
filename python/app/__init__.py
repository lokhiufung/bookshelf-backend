from fastapi import FastAPI

from app.items import Book



app = FastAPI()

library = dict()  # temp

@app.get('/')
async def index():
    return {
        'hello': 'world'
    }


@app.post('/book/add')
def add_book(book: Book):
    book_dict = book.dict()
    library[book.title] = book_dict
    return {
        'status': 'added',
    } 
        

@app.post('/book/{_id}')
def add_book(book: Book):
    book_dict = book.dict()
    library[book.title] = book_dict
    return {
        'status': 'added',
    } 
