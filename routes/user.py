from fastapi import Body, APIRouter, HTTPException
from passlib.context import CryptContext

from auth.jwt_handler import sign_jwt
from database.user import add_user
from models.User import User
from schemas.user import UserData, UserSignIn

router = APIRouter()

hash_helper = CryptContext(schemes=["bcrypt"])


@router.post("/login")
async def user_login(user_credentials: UserSignIn = Body(...)):
    user_exists = await User.find_one(User.username == user_credentials.username)
    if user_exists:
        password = hash_helper.verify(user_credentials.password, user_exists.password)
        if password:
            return sign_jwt(user_credentials.username)

        raise HTTPException(status_code=403, detail="Incorrect email or password")

    raise HTTPException(status_code=403, detail="Incorrect email or password")


@router.post("/", response_model=UserData)
async def user_signup(user: User = Body(...)):
    user_exists = await User.find_one(User.username == user.username)
    if user_exists:
        raise HTTPException(
            status_code=409, detail="User with email supplied already exists"
        )

    user.password = hash_helper.encrypt(user.password)
    new_user = await add_user(user)
    return new_user
