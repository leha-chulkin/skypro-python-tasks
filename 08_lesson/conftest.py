import pytest
from config import API_BASE_URL
import requests

# --- ФИКСТУРА: очистка данных после каждого теста ---
@pytest.fixture(autouse=True)
def cleanup_project():
    """Очищает все созданные проекты после каждого теста."""
    # Получаем список всех проектов
    response = requests.get(f"{API_BASE_URL}/projects")
    if response.status_code == 200:
        projects = response.json()
        for project in projects:
            project_id = project.get('id')
            if project_id:
                # Удаляем проект
                delete_response = requests.delete(f"{API_BASE_URL}/projects/{project_id}")
                if delete_response.status_code != 204:
                    print(f"Не удалось удалить проект {project_id}:{delete_response.status_code}")
    else:
        print("Не удалось получить список проектов для очистки")
