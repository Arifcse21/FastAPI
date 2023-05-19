from crud.models import Base
from fastapi import FastAPI
from .db_connection import Database
from crud.routers import create_user_router
from crud.routers import get_users_router
from crud.routers import get_individual_user_router
from crud.routers import delete_user_router
from crud.routers import update_user_router


db = Database()
engine, session = db()
Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(get_users_router)
app.include_router(create_user_router)
app.include_router(get_individual_user_router)
app.include_router(delete_user_router)
app.include_router(update_user_router)





