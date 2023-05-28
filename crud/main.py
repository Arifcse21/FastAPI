from crud.models import Base
from fastapi import FastAPI
from .db_connection import Database
from crud.routers import create_user_router
from crud.routers import get_users_router
from crud.routers import get_individual_user_router
from crud.routers import delete_user_router
from crud.routers import update_user_router


db = Database()
engine, session = db()
Base.metadata.create_all(engine)

description = """
        Crud App API helps you do awesome stuff. 🚀
        
        ## Items
        
        You can **read items**.
        
        ## Users
        
        You will be able to:
        
        * **Create users** (_not implemented_).
        * **Read users** (_not implemented_).
    """

app = FastAPI(
    title="Crud App",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Deadpoolio the Amazing",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

app.include_router(get_users_router)
app.include_router(create_user_router)
app.include_router(get_individual_user_router)
app.include_router(delete_user_router)
app.include_router(update_user_router)





