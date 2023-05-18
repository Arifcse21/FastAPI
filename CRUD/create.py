from fastapi import FastAPI
from db_connection import Database
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from tables import Base, User
from pydantic import BaseModel

app = FastAPI()

db = Database()
engine = db()
ssson = sessionmaker(bind=engine)
session = ssson()

Base.metadata.create_all(engine)


class NewUser(BaseModel):
    fullname: str | None = None
    email: str | None = None
    phone: str | None = None
    address: str | None = None
    NID: str | None = None


@app.post("/add-user/")
def create_user(user: NewUser):
    print(f"{Database()}")
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


