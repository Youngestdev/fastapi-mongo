import asyncio
from beanie import init_beanie
from fastapi.testclient import TestClient
from httpx import AsyncClient
import pytest

from models.admin import Admin
from models.contact import Contact
from tests.conftest import mock_no_authentication


class TestMockAuthentication:
    @classmethod
    def setup_class(cls):
        mock_no_authentication()

    @pytest.mark.anyio
    async def test_mock_databases(self, client_test: AsyncClient):
        # generate data
        await Admin(
            fullname="admin", email="admin@admin.com", password="admin"
        ).create()

        await Contact(
            fullname="contact mock",
            email="mock@contact.com",
            message="tengo un problema, un problema sexual"
        ).create()

        response = await client_test.get("contact")

        assert response.status_code == 200

    @pytest.mark.anyio
    async def test_mock_database(self, client_test: AsyncClient):
        await Admin(
            fullname="admin", email="admin@admin.com", password="admin"
        ).create()

        await Contact(
            fullname="contact",
            email="mock2@contact.com",
            course_of_study="mock2"
        ).create()

        response = await client_test.get("contact")

        assert response.status_code == 200
