from fastapi import Body, APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBasicCredentials
from passlib.context import CryptContext

from app.server.auth.admin import validate_login
from app.server.auth.jwt_handler import signJWT
from app.server.database.database import add_admin
from app.server.models.admin import AdminModel

router = APIRouter()

hash_helper = CryptContext(schemes=["bcrypt"])

@router.post("/login")
async def admin_login(admin: HTTPBasicCredentials = Body(...)):
    if validate_login(admin):
        return {
            "email": admin.username,
            "access_token": signJWT(admin.username)
        }
    return "Invalid Login Details!"

@router.post("/")
async def admin_signup(admin: AdminModel = Body(...)):
    # TODO: Perform validation to check if user exists.
    admin.password = hash_helper.encrypt(admin.password)
    new_admin = await add_admin(jsonable_encoder(admin))
    return new_admin