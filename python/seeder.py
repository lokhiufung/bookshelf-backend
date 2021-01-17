import pymongo

from app import config


def main():
    # initialize a database

    db_name = config.DATABASE_NAME
    col_name = config.BOOK_COLLECTION
    
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client[db_name]
    col= db[col_name]

    col.insert_one({
        'title': '<seeder-book>',
        'url': 'https://<seeder-book>',
        'description': '<seeder-book>',
        'tags': [],
        'book_id': "0000"
    })
    client.close()
    print(f'created a database {db_name} and a collection {col_name}')
    
    # remove seeder doc from db
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client[db_name]
    col= db[col_name]
    col.delete_many({})  # remove all docs
    client.close()
    print(f'removed all seeder docs from the database {db_name} and collection {col_name}')

    

if __name__ == '__main__':
    main()
    