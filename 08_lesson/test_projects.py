import requests
from config import API_BASE_URL


def test_create_project():
    """Тест создания проекта."""
    payload = {
        "name": "Test Project 1",
        "description": "Test description"
    }
    response = requests.post(f"{API_BASE_URL}/projects", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Project 1"


def test_get_project_by_id():
    """Тест получения проекта по ID."""
    # Создаём проект
    payload = {
        "name": "Test Project 2",
        "description": "Another test"
    }
    create_response = requests.post(f"{API_BASE_URL}/projects", json=payload)
    project_id = create_response.json()["id"]

    # Получаем его
    get_response = requests.get(f"{API_BASE_URL}/projects/{project_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["id"] == project_id


def test_update_project():
    """Тест обновления проекта."""
    payload = {
        "name": "Test Project 3",
        "description": "Initial"
    }
    create_response = requests.post(f"{API_BASE_URL}/projects", json=payload)
    project_id = create_response.json()["id"]

    update_payload = {
        "name": "Updated Project 3",
        "description": "Updated description"
    }
    update_response = requests.put(f"{API_BASE_URL}/projects/{project_id}", json=update_payload)
    assert update_response.status_code == 200
    data = update_response.json()
    assert data["name"] == "Updated Project 3"


def test_delete_project():
    """Тест удаления проекта."""
    payload = {
        "name": "Test Project 4",
        "description": "To be deleted"
    }
    create_response = requests.post(f"{API_BASE_URL}/projects", json=payload)
    project_id = create_response.json()["id"]

    delete_response = requests.delete(f"{API_BASE_URL}/projects/{project_id}")
    assert delete_response.status_code == 204

    # Проверяем, что проект удалён
    get_response = requests.get(f"{API_BASE_URL}/projects/{project_id}")
    assert get_response.status_code == 404
