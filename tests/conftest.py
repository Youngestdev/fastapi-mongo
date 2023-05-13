"""Tests fixtures."""
import pytest
from asgi_lifespan import LifespanManager
from httpx import AsyncClient

from app import app

@pytest.fixture
async def client_test():
    """
    Create an instance of the client.
    :return: yield HTTP client.
    """
    async with LifespanManager(app):
        async with AsyncClient(
            app=app, base_url="http://test", follow_redirects=True
        ) as ac:
            yield ac

@pytest.fixture
def anyio_backend():
    return 'asyncio'
