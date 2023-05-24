import pytest
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from .user_model import User


def test_create_user(session):
    user = User(
        fullname="test_user",
        email="user@hotmail.com",
        phone="+692324252525",
        address="Somewhere in nowhere",
        NID="123456778452"
    )
    session.add(user)
    session.commit()

    assert user.id == 1
    assert user.fullname == "test_user"


def test_create_user_with_existing_email(session, demo_user):
    new_user = User(
        fullname="demo_user_1",
        email="demo_user@hotmail.com",
        phone="+6923242322525",
        address="Somewhere in nowhere you know",
        NID="123456778452"
    )
    session.add(new_user)
    with pytest.raises(IntegrityError):
        session.commit()


def test_find_user_by_email(session):
    new_user = User(
        fullname="new_user_1",
        email="new_user@hotmail.com",
        phone="+69232442322525",
        address="Somewhere in nowhere you know",
        NID="1234546778452"
    )
    session.add(new_user)
    session.commit()

    find_user = session.query(User).filter_by(email="new_user@hotmail.com").first()

    assert find_user == new_user


def test_delete_user(session):
    new_user = User(
        fullname="new_user_1",
        email="delete_user@hotmail.com",
        phone="+69232442322525",
        address="Somewhere in nowhere you know",
        NID="1234546778452"
    )
    session.add(new_user)
    session.commit()

    session.delete(new_user)
    session.commit()

    result = session.query(User).filter_by(email="delete_user@hotmail.com").first()

    assert result is None
