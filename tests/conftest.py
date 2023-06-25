"""Tests fixtures."""
from beanie import init_beanie
import pytest
from asgi_lifespan import LifespanManager
from httpx import AsyncClient

from app import app
from mongomock_motor import AsyncMongoMockClient
from config.config import initiate_database

import models as models
from app import app, token_listener


async def mock_database():
    client = AsyncMongoMockClient()
    await init_beanie(
        database=client["database_name"],
        recreate_views=True,
        document_models=models.__all__,
    )


def mock_no_authentication():
    app.dependency_overrides[token_listener] = lambda: {}


@pytest.fixture
async def client_test(mocker):
    """
    Create an instance of the client.
    :return: yield HTTP client.
    """

    mocker.patch("config.config.initiate_database", return_value=await mock_database())

    async with LifespanManager(app):
        async with AsyncClient(
            app=app, base_url="http://test", follow_redirects=True
        ) as ac:
            yield ac


@pytest.fixture
def anyio_backend():
    return "asyncio"
