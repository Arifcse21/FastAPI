from fastapi.testclient import TestClient
from fastapi import FastAPI
import pytest

app = FastAPI()
client = TestClient(app)
print(client)


def test_create_user():
    payload = {
        "fullname": "test_user_bro",
        "email": "bro_vai@bromail.com",
        "phone": "+3343432523523",
        "address": "Bro Zone",
        "NID": "1234567464"
    }

    # resp = client.post(data=payload, url="/add-user/")

    # print(resp)
    # assert resp.status_code == 201
