from fastapi.testclient import TestClient
from httpx import AsyncClient
import pytest

from app import app, token_listener

### Mocking the authentication to no check###
async def fake_authentication():
    return {}

app.dependency_overrides[token_listener] = fake_authentication
###################################


@pytest.mark.anyio
async def test_api_processed_jobs(client_test: AsyncClient):
    response = await client_test.get("student")

    assert response.status_code == 200

