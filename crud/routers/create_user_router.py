from fastapi import APIRouter
from ..db_connection import Database
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from crud.models import Base, User
from crud.schemas import NewUser


db = Database()
engine, session = db()

new_user_router = APIRouter()


@new_user_router.post("/add-user/", tags=['users'])
def create_user(user: NewUser):
    new_user = User(
        fullname=user.fullname,
        email=user.email,
        phone=user.phone,
        address=user.address,
        NID=user.NID
    )
    session.add(new_user)
    session.commit()

    response = {
        "status": "successful",
        "message": "new user created",
        "data": user
    }

    return response


