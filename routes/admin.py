from fastapi import Body, APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBasicCredentials
from passlib.context import CryptContext

from database.database import admin_collection
from auth.jwt_handler import signJWT
from database.database import add_admin
from models.admin import AdminModel

router = APIRouter()

hash_helper = CryptContext(schemes=["bcrypt"])

@router.post("/login")
async def admin_login(admin_credentials: HTTPBasicCredentials = Body(...)):
    # NEW CODE
    admin_user = await admin_collection.find_one({"email": admin_credentials.username}, {"_id": 0})
    if (admin_user):
        password = hash_helper.verify(
            admin_credentials.password, admin_user["password"])
        if (password):
            return signJWT(admin_credentials.username)

        return "Incorrect email or password"

    return "Incorrect email or password"

@router.post("/")
async def admin_signup(admin: AdminModel = Body(...)):
    admin_exists = await admin_collection.find_one({"email":  admin.email}, {"_id": 0})
    if(admin_exists):
        return "Email already exists"
    
    admin.password = hash_helper.encrypt(admin.password)
    new_admin = await add_admin(jsonable_encoder(admin))
    return new_admin