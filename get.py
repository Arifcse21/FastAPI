from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()


@app.get("/")
def home():
    return {"Data": "Testing"}


@app.get("/about")
def about():
    return {"Data": "About"}


inventory = {
    1: {
        "name": "Bread",
        "price": 2,
        "brand": "regular"
    }
}


@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return inventory[item_id]

# @app.get("/get-item/{item_id}/{name}")
# def get_item(item_id : int, name : str):
#     ## multiple path parameters
#     return inventory[item_id]


# @app.get("/get-item/{item_id}")
# def get_item(item_id: int = Path(None, description="The id of the item you want to see")):
#     return inventory[item_id]


# @app.get("/get-by-name")
# # def get_item(name : str):
# # def get_item(test : int, name: Optional[str] = None):
# def get_item(*, name: Optional[str] = None, test : int):
#     # localhost:8000/get-by-name?test=1&name=Bread
#     # query parameters
#     for item_id in inventory:
#         if inventory[item_id]["name"] == name:
#             return  inventory[item_id]
#     return {"Data": "Item Not Found"}


# @app.get("/get-by-name/{item_id}")
# def get_item(*, item_id: int, name: Optional[str] = None, test: int):
#     # localhost:8000/get-by-name/1?test=1&name=Bread
#     # query parameters with path parameters
#     for item_id in inventory:
#         if inventory[item_id]["name"] == name:
#             return inventory[item_id]
#     return {"Data": "Item Not Found"}
