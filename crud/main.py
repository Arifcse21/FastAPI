from crud.models import Base
from fastapi import FastAPI
from .db_connection import Database
from crud.routers.create_user_router import create_user_router
from crud.routers.get_users_router import get_users_router
from crud.routers.individual_user_router import get_individual_user_router
from crud.routers.delete_user_router import delete_user_router


db = Database()
engine, session = db()
Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(get_users_router)
app.include_router(create_user_router)
app.include_router(get_individual_user_router)
app.include_router(delete_user_router)





