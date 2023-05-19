from fastapi import APIRouter, status
from crud.models import Base, User
from crud.schemas import UserSchema
from ..db_connection import Database
from sqlalchemy import update
from fastapi.encoders import jsonable_encoder

db = Database()
engine, session = db()
update_user_router = APIRouter()


@update_user_router.put("/user/update/{user_id}", tags=["users"], status_code=status.HTTP_200_OK)
def update_individual_user(update_user: UserSchema, user_id: int):
    try:
        update_data = update_user.dict(exclude_unset=True)
        print(f"{update_data}")
        user = update(User).where(User.id == user_id).values(**update_data)   # unpack update_data dictionary
        session.execute(user)
        session.commit()
        response = {
            "status": "successful",
            "code": status.HTTP_200_OK,
            "message": "User data updated successfully",
        }
        return response

    except Exception as e:
        response = {
            "status": "failed",
            "code": status.HTTP_400_BAD_REQUEST,
            "message": str(e),
        }
        return response
