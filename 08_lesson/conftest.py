import requests
from typing import Generator, Dict, Any, List  # ✅ Исправлено: добавлен List
import pytest

# --- Конфигурация API ---
BASE_URL = "https://ru.yougile.com/api-v2"
AUTH_TOKEN = "ebacR8vN8GsMnY2inIE-xNxwIROCfU1xH9kRUcE3eP8yS3pZ5X1vgwnZHrdl7YJ9"

# --- Фикстура session ---
@pytest.fixture
def session() -> Generator[requests.Session, None, None]:
    """Сессия с авторизацией для всех запросов."""
    s = requests.Session()
    s.headers.update({
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Content-Type": "application/json"
    })
    s.base_url = BASE_URL  # Добавляем кастомное поле для удобства
    yield s
    s.close()


# --- Фикстура project_data ---
@pytest.fixture
def project_data() -> Dict[str, Any]:
    return {
        "title": "Тестовый проект",
        "users": {}  # Обязательно! API требует поле users, даже если пусто
    }


# --- Фикстура updated_project_data ---
@pytest.fixture
def updated_project_data() -> Dict[str, Any]:
    return {
        "title": "Обновлённый тестовый проект",
        "users": {}
    }


# --- Фикстура cleanup_project ---
@pytest.fixture
def cleanup_project(session: requests.Session) -> Generator[None, None, None]:
    """Автоматически удаляет созданные проекты после теста."""
    created_ids: List[str] = []  # ✅ Теперь List определён

    def _add_project_id(project_id: str) -> None:
        created_ids.append(project_id)

    yield _add_project_id

    # Cleanup: удалить все созданные проекты
    for proj_id in created_ids:
        response = session.delete(f"{BASE_URL}/projects/{proj_id}")
        if response.status_code != 204:
            print(f"⚠️ Не удалось удалить проект с ID {proj_id}: {response.status_code} {response.text}")
