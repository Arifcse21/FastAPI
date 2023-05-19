from fastapi import APIRouter, status
from crud.models import Base, User
from ..db_connection import Database
from sqlalchemy import select
from fastapi.encoders import jsonable_encoder

db = Database()
engine, session = db()
get_users_router = APIRouter()


@get_users_router.get("/get_users/", tags=["users"], status_code=status.HTTP_200_OK)
def get_users():
    try:
        users = select(User)

        results = session.execute(users).fetchall()
        print(f"Here::::: {results}")
        response = {
            "status": "successful",
            "code": status.HTTP_200_OK,
            "message": "All users list",
            "data": [jsonable_encoder(obj[0].__dict__) for obj in results]
        }
        return response

    except Exception as e:
        response = {
            "status": "failed",
            "code": status.HTTP_400_BAD_REQUEST,
            "message": str(e),
        }
        return response
