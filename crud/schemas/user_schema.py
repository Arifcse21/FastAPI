from pydantic import BaseModel


class UserSchema(BaseModel):
    fullname: str | None = None
    email: str | None = None
    phone: str | None = None
    address: str | None = None
    NID: str | None = None

