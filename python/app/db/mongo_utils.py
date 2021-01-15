import os

from motor.motor_asyncio import AsyncIOMotorClient

from .mongodb import db

DB_HOST = os.environ.get('DB_HOST', '0.0.0.0')
DB_PORT = os.environ.get('DB_PORT', 27017)


async def connect_to_mongo():
    db.client = AsyncIOMotorClient(host=DB_HOST, port=DB_PORT)


async def close_mongo_connection():
    db.client.close()