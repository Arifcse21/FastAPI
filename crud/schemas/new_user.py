from pydantic import BaseModel


class NewUser(BaseModel):
    fullname: str | None = None
    email: str | None = None
    phone: str | None = None
    address: str | None = None
    NID: str | None = None

