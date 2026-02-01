import pytest
import requests
from typing import Dict, Any

@pytest.fixture
def cleanup_project(session):
    deleted_ids = []

    def _add_project_id(project_id):
        deleted_ids.append(project_id)

    yield _add_project_id

    for project_id in deleted_ids:
        response = session.delete(f"{session.base_url}/projects/{project_id}")
        if response.status_code != 404:
            assert response.status_code == 204, f"Failed to delete project {project_id}"

def test_create_and_get_project(session: requests.Session, project_data: Dict[str, Any], cleanup_project) -> None:
    response = session.post(f"{session.base_url}/projects", json=project_data)
    assert response.status_code == 201
    project_id = response.json()["id"]
    cleanup_project(project_id)

    response = session.get(f"{session.base_url}/projects/{project_id}")
    assert response.status_code == 200
    assert response.json()["title"] == project_data["title"]

def test_update_project(session: requests.Session, project_data: Dict[str, Any], updated_project_data: Dict[str, Any], cleanup_project) -> None:
    response = session.post(f"{session.base_url}/projects", json=project_data)
    assert response.status_code == 201
    project_id = response.json()["id"]
    cleanup_project(project_id)

    full_update_data = {
        "title": updated_project_data["title"],
        "users": project_data["users"]
    }

    response = session.put(f"{session.base_url}/projects/{project_id}", json=full_update_data)
    assert response.status_code == 200
    updated = response.json()
    assert updated["title"] == updated_project_data["title"]

def test_get_projects_list(session: requests.Session) -> None:
    response = session.get(f"{session.base_url}/projects")
    assert response.status_code == 200
    projects = response.json()
    assert isinstance(projects, list)

def test_create_project_without_title(session: requests.Session) -> None:
    invalid_data = {"users": {}}
    response = session.post(f"{session.base_url}/projects", json=invalid_data)
    assert response.status_code == 400
    response_json = response.json()
    assert "title" in response_json.get("message", "").lower() or "обязательно" in response_json.get("message", "").lower()

def test_update_nonexistent_project(session: requests.Session, updated_project_data: Dict[str, Any]) -> None:
    invalid_id = "00000000-0000-0000-0000-000000000000"
    response = session.put(f"{session.base_url}/projects/{invalid_id}", json=updated_project_data)
    assert response.status_code == 404
    assert response.json().get("message") == "Проект не найден"

def test_get_nonexistent_project(session: requests.Session) -> None:
    invalid_id = "11111111-1111-1111-1111-111111111111"
    response = session.get(f"{session.base_url}/projects/{invalid_id}")
    assert response.status_code == 404
    assert response.json().get("message") == "Проект не найден"
