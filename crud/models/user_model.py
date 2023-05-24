from sqlalchemy import Column, Integer, String
from typing import Optional
from sqlalchemy.orm import (
    DeclarativeBase, mapped_column, Mapped
)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "User"
    id: Mapped[int] = mapped_column(primary_key=True)
    fullname: Mapped[str]
    email: Mapped[str] = mapped_column(String(100), unique=True)
    phone: Mapped[str] = mapped_column(String(100))
    address: Mapped[str] = mapped_column(String(200))
    NID: Mapped[str] = mapped_column(String(30))

    def __repr__(self):
        return f"""
            User(id={self.id!r}, 
            fullname={self.fullname!r}, 
            email={self.email!r}, 
            phone={self.phone!r}, 
            address={self.address!r}
            NID={self.NID!r}
            )
        """





