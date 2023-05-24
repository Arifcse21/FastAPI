import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .user_model import Base, User

_TEST_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"


@pytest.fixture(scope="module")
def engine():
    return create_engine(_TEST_DATABASE_URL)


@pytest.fixture(scope="module")
def tables(engine):
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


@pytest.fixture
def session(engine, tables):
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    yield Session()
    transaction.rollback()
    connection.close()


@pytest.fixture
def demo_user(session):
    demo_user_1 = User(
        fullname="demo_user_1",
        email="demo_user@hotmail.com",
        phone="+6923242322525",
        address="Somewhere in nowhere you know",
        NID="123456778452"
    )
    session.add(demo_user_1)
    session.commit()
