from fastapi import FastAPI, Depends

# from auth.jwt_bearer import JWTBearer
from config.config import init_database
from routes.user import router as UserRouter
# from routes.student import router as StudentRouter

app = FastAPI()

# token_listener = JWTBearer()


@app.on_event("startup")
async def start_database():
    await init_database()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}


app.include_router(UserRouter, tags=["User"], prefix="/users")
# app.include_router(StudentRouter,tags=["Students"],prefix="/student",dependencies=[Depends(token_listener)],)
