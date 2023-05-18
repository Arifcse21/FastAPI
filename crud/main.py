from crud.models import Base
from fastapi import FastAPI
from crud.routers.create_user_router import new_user_router

app = FastAPI()

app.include_router(new_user_router)




