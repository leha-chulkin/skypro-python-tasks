import pytest
import requests
from config import AUTH_TOKEN


@pytest.fixture(scope="session")
def auth_token():
    return AUTH_TOKEN


@pytest.fixture(scope="session")
def base_url():
    return "https://x-clients-be.onrender.com"


@pytest.fixture(scope="function")
def company_id(auth_token, base_url):
    headers = {"Authorization": f"Bearer {auth_token}"}
    body = {
        "name": "Тестовая компания",
        "description": "Для автотестов"
    }
    response = requests.post(
        f"{base_url}/company", json=body, headers=headers
    )
    company_id = response.json()["id"]
    yield company_id
    requests.delete(f"{base_url}/company/{company_id}", headers=headers)
