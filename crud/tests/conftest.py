import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crud.models import Base
from crud.db_connection import Database


@pytest.fixture(scope="module")
def db():
    db = Database()
    return db


@pytest.fixture(scope="module")
def models(db):
    engine, session = db()
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


@pytest.fixture
def session(db, models):
    engine, session = db()
    connection = engine.connect()
    transaction = connection.begin()
    yield session()
    transaction.rollback()
    connection.close()



