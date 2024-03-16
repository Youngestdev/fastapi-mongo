from beanie import Document
from fastapi.security import HTTPBasicCredentials
from pydantic import BaseModel


class User(Document):
    firstname: str
    lastname: str
    username: str
    password: str

    class Settings:
        name = "users"

