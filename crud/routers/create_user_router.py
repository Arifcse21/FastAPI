from fastapi import APIRouter, status
from ..db_connection import Database
from crud.models import Base, User
from crud.schemas import UserSchema


db = Database()
engine, session = db()

create_user_router = APIRouter()


@create_user_router.post("/add-user/", tags=['users'], status_code=status.HTTP_201_CREATED)
def create_user(user: UserSchema):
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
        "code": status.HTTP_201_CREATED,
        "message": "new user created",
        "data": user
    }

    return response


