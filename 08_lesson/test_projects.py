# test_project_api.py — ПОСЛЕ ИСПРАВЛЕНИЯ


# --- ПОЗИТИВНЫЕ ТЕСТЫ ---
def test_post_project_positive(session, project_data):
    response = session.post("/projects", json=project_data)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == project_data["title"]
    assert "id" in data
    assert data["completed"] is False

def test_put_project_positive(session, project_data, updated_project_data):
    post_response = session.post("/projects", json=project_data)
    project_id = post_response.json()["id"]
    put_response = session.put(f"/projects/{project_id}", json=updated_project_data)
    assert put_response.status_code == 200
    data = put_response.json()
    assert data["title"] == updated_project_data["title"]
    assert data["completed"] == updated_project_data["completed"]

def test_get_project_positive(session, project_data):
    post_response = session.post("/projects", json=project_data)
    project_id = post_response.json()["id"]
    get_response = session.get(f"/projects/{project_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["id"] == project_id
    assert data["title"] == project_data["title"]

# --- НЕГАТИВНЫЕ ТЕСТЫ ---
def test_post_project_negative_missing_title(session):
    payload = {"completed": False}
    response = session.post("/projects", json=payload)
    assert response.status_code == 400
    assert "title" in response.json().get("detail", "")

def test_put_project_negative_invalid_id(session, updated_project_data):
    invalid_id = 999999999
    response = session.put(f"/projects/{invalid_id}", json=updated_project_data)
    assert response.status_code == 404
    assert "Project not found" in response.text

def test_get_project_negative_invalid_id(session):
    invalid_id = 999999999
    response = session.get(f"/projects/{invalid_id}")
    assert response.status_code == 404
    assert "Project not found" in response.text
