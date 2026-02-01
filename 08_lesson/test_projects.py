# test_projects.py
import pytest
import requests
from config import API_BASE_URL, INVALID_PROJECT_ID
from conftest import headers, session, project_data, updated_project_data, cleanup_project


# =============================
# [POST] /api-v2/projects
# =============================

def test_post_project_positive(session, project_data, cleanup_project):
    """Позитивный тест: создание проекта"""
    response = session.post(f"{API_BASE_URL}/projects", json=project_data)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"
    data = response.json()
    assert "id" in data, "Response should contain 'id'"
    assert data["title"] == project_data["title"], "Title mismatch"

    # Регистрируем проект для удаления
    cleanup_project(data["id"])


def test_post_project_negative_missing_title(session):
    """Негативный тест: создание проекта без обязательного поля title"""
    invalid_data = {"description": "No title here", "isArchived": False}
    response = session.post(f"{API_BASE_URL}/projects", json=invalid_data)
    assert response.status_code == 400, f"Expected 400 for missing title, got {response.status_code}"
    error = response.json()
    assert "errors" in error, "Should return validation errors"
    assert any("title" in err.get("field", "") for err in error["errors"]), "Should mention 'title' in errors"


# =============================
# [PUT] /api-v2/projects/{id}
# =============================

def test_put_project_positive(session, updated_project_data, cleanup_project):
    """Позитивный тест: обновление существующего проекта"""
    # Создаём проект
    response = session.post(f"{API_BASE_URL}/projects", json=updated_project_data)
    assert response.status_code == 201
    project_id = response.json()["id"]
    cleanup_project(project_id)  # Регистрируем для удаления

    # Обновляем
    response = session.put(f"{API_BASE_URL}/projects/{project_id}", json=updated_project_data)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    assert data["title"] == updated_project_data["title"], "Title was not updated"


def test_put_project_negative_invalid_id(session, updated_project_data):
    """Негативный тест: обновление несуществующего проекта"""
    response = session.put(f"{API_BASE_URL}/projects/{INVALID_PROJECT_ID}", json=updated_project_data)
    assert response.status_code == 404, f"Expected 404 for invalid project ID, got {response.status_code}"
    error = response.json()
    assert error.get("message") == "Project not found", "Error message should indicate project not found"


# =============================
# [GET] /api-v2/projects/{id}
# =============================

def test_get_project_positive(session, cleanup_project):
    """Позитивный тест: получение существующего проекта"""
    # Создаём проект
    response = session.post(f"{API_BASE_URL}/projects", json=project_data)
    assert response.status_code == 201
    project_id = response.json()["id"]
    cleanup_project(project_id)  # Регистрируем для удаления

    # Получаем
    response = session.get(f"{API_BASE_URL}/projects/{project_id}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    assert data["id"] == project_id, "Returned project ID doesn't match"
    assert "title" in data, "Response should contain title"


def test_get_project_negative_invalid_id(session):
    """Негативный тест: получение несуществующего проекта"""
    response = session.get(f"{API_BASE_URL}/projects/{INVALID_PROJECT_ID}")
    assert response.status_code == 404, f"Expected 404 for invalid project ID, got {response.status_code}"
    error = response.json()
    assert error.get("message") == "Project not found", "Error message should indicate project not found"
