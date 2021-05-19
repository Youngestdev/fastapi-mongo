from fastapi import FastAPI, Depends

from auth.jwt_bearer import JWTBearer
from routes.student import router as StudentRouter
from routes.admin import router as AdminRouter

app = FastAPI()

token_listener = JWTBearer()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}


app.include_router(AdminRouter, tags=["Administrator"], prefix="/admin")
app.include_router(StudentRouter, tags=["Students"], prefix="/student", dependencies=[Depends(token_listener)])
