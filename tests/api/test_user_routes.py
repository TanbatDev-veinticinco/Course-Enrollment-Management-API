from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_user_success():
    response = client.post(
        "/users/",
        json={
            "name": "John",
            "email": "john@test.com",
            "role": "student"
        }
    )

    assert response.status_code == 201
    data = response.json()

    assert data["name"] == "John"
    assert data["email"] == "john@test.com"
    assert data["role"] == "student"
    assert "id" in data

def test_create_user_duplicate_email():
    client.post(
        "/users/",
        json={
            "name": "Jane",
            "email": "duplicate@test.com",
            "role": "student"
        }
    )

    response = client.post(
        "/users/",
        json={
            "name": "Jane2",
            "email": "duplicate@test.com",
            "role": "student"
        }
    )

    assert response.status_code == 400


def test_get_all_users():
    response = client.get("/users/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_user_by_id():
    create = client.post(
        "/users/",
        json={
            "name": "Mark",
            "email": "mark@test.com",
            "role": "admin"
        }
    )

    user_id = create.json()["id"]

    response = client.get(f"/users/{user_id}")

    assert response.status_code == 200
    assert response.json()["id"] == user_id

def test_get_user_not_found():
    response = client.get("/users/9999")

    assert response.status_code == 404