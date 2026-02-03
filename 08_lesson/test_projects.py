import requests


def test_get_employee_list(auth_token, base_url, company_id):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(
        f"{base_url}/employee?company={company_id}", headers=headers
    )
    assert response.status_code == 200
    employees = response.json()
    assert isinstance(employees, list)


def test_create_employee(auth_token, base_url, company_id):
    headers = {"Authorization": f"Bearer {auth_token}"}
    body = {
        "firstName": "Иван",
        "lastName": "Петров",
        "middleName": "Сергеевич",
        "companyId": company_id,
        "email": "ivan@test.ru",
        "url": "http://example.com",
        "phone": "79991234567",
        "birthdate": "1990-01-01",
        "isActive": True
    }
    response = requests.post(
        f"{base_url}/employee", json=body, headers=headers
    )
    assert response.status_code == 201
    employee = response.json()
    assert employee["id"] > 0
    assert employee["firstName"] == "Иван"


def test_get_employee_by_id(auth_token, base_url, company_id):
    headers = {"Authorization": f"Bearer {auth_token}"}
    body = {
        "firstName": "Анна",
        "lastName": "Сидорова",
        "companyId": company_id,
        "isActive": True
    }
    create_response = requests.post(
        f"{base_url}/employee", json=body, headers=headers
    )
    employee_id = create_response.json()["id"]
    response = requests.get(
        f"{base_url}/employee/{employee_id}", headers=headers
    )
    assert response.status_code == 200
    employee = response.json()
    assert employee["id"] == employee_id
    assert employee["firstName"] == "Анна"


def test_update_employee(auth_token, base_url, company_id):
    headers = {"Authorization": f"Bearer {auth_token}"}
    body = {
        "firstName": "Петр",
        "lastName": "Иванов",
        "companyId": company_id,
        "isActive": True
    }
    create_response = requests.post(
        f"{base_url}/employee", json=body, headers=headers
    )
    employee_id = create_response.json()["id"]
    update_body = {
        "lastName": "Смирнов",
        "email": "petr@test.ru",
        "url": "http://new-site.com",
        "phone": "79997654321"
    }
    response = requests.patch(
        f"{base_url}/employee/{employee_id}",
        json=update_body,
        headers=headers
    )
    assert response.status_code == 200
    updated_employee = response.json()
    assert updated_employee["lastName"] == "Смирнов"
    assert updated_employee["email"] == "petr@test.ru"
