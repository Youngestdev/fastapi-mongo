from models.User import User


async def add_user(new_user: User) -> User:
    user = await new_user.create()
    return user
