from fastapi import APIRouter, status
from crud.models import Base, User
from crud.schemas import UserSchema
from ..db_connection import Database
from sqlalchemy import select
from fastapi.encoders import jsonable_encoder

db = Database()
engine, session = db()
get_individual_user_router = APIRouter()


@get_individual_user_router.get("/user/{user_id}", tags=["users"], status_code=status.HTTP_200_OK)
def get_individual_user(user_id: int):
    try:
        users = select(User).filter(User.id == user_id)

        result = session.execute(users).fetchall()
        response = {
            "status": "successful",
            "code": status.HTTP_200_OK,
            "message": "Individual user data",
            "data": [jsonable_encoder(obj[0].__dict__) for obj in result]
        }
        return response

    except Exception as e:
        response = {
            "status": "failed",
            "code": status.HTTP_400_BAD_REQUEST,
            "message": str(e),
        }
        return response
