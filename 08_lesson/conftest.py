# conftest.py
import pytest
import requests
from config import API_BASE_URL, API_TOKEN

@pytest.fixture
def headers():
    return {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

@pytest.fixture
def session(headers):
    session = requests.Session()
    session.headers.update(headers)
    return session

@pytest.fixture
def project_data():
    return {
        "title": "Test Project for Automation",
        "description": "Created by automated test",
        "isArchived": False
    }

@pytest.fixture
def updated_project_data():
    return {
        "title": "Updated Test Project for Automation",
        "description": "Updated by automated test",
        "isArchived": False
    }
