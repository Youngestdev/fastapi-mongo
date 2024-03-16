from typing import Optional

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic_settings import BaseSettings
import models as models


class Settings(BaseSettings):
    # database configurations
    DATABASE_URL: Optional[str] = None
    JWT_SECRET_KEY: Optional[str]= None

    class Config:
        env_file = ".env.dev"
        from_attributes = True


async def init_database():
    print(Settings().DATABASE_URL)
    client = AsyncIOMotorClient(Settings().DATABASE_URL)
    await init_beanie(
        database=client.get_default_database(), document_models=models.__all__
    )
