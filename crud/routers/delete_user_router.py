from fastapi import APIRouter, status
from crud.models import Base, User
from crud.schemas import UserSchema
from ..db_connection import Database
from sqlalchemy import delete
from fastapi.encoders import jsonable_encoder

db = Database()
engine, session = db()
delete_user_router = APIRouter()


@delete_user_router.delete("/user/{user_id}", tags=["users"], status_code=status.HTTP_200_OK)
def get_individual_user(user_id: int):
    try:
        user = delete(User).filter(User.id == user_id)
        session.execute(user)
        session.commit()
        response = {
            "status": "successful",
            "code": status.HTTP_200_OK,
            "message": "Individual user deleted",
        }
        return response

    except Exception as e:
        response = {
            "status": "failed",
            "code": status.HTTP_400_BAD_REQUEST,
            "message": str(e),
        }
        return response
