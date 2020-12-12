from fastapi import FastAPI

# from 
from .db.mongo_utils import close_mongo_connection, connect_to_mongo

app = FastAPI()


app.add_event_handler('startup', connect_to_mongo)
app.add_event_handler('shutdown', close_mongo_connection)

app.include_router()
