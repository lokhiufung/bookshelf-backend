import pymongo

from app import config


def main():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client[config.DATABASE_NAME]
    col= db[config.BOOK_COLLECTION]

    col.insert_one({
        'title': '<seeder-book>',
        'url': 'https://<seeder-book>',
        'description': '<seeder-book>',
        'tags': [],
        'book_id': "0000"
    })

if __name__ == '__main__':
    main()
    