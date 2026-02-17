from fastapi.testclient import TestClient
from main import app
import pytest
from app.storage import database

client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_data():
    database.users.clear()
    database.courses.clear()
    database.enrollments.clear()
    yield


def create_student():
    response = client.post(
        "/users/",
        json={
            "name": "John",
            "email": "john@test.com",
            "role": "student"
        }
    )
    return response.json()["id"]


def create_course():
    response = client.post(
        "/courses/?role=admin",
        json={
            "title": "Math",
            "code": "MTH101"
        }
    )
    return response.json()["id"]


def test_student_can_enroll():
    user_id = create_student()
    course_id = create_course()

    response = client.post(
        "/enrollments/",
        json={
            "user_id": user_id,
            "course_id": course_id,
            "role": "student"
        }
    )

    assert response.status_code == 201
    data = response.json()

    assert data["user_id"] == user_id
    assert data["course_id"] == course_id


def test_student_cannot_enroll_twice():
    user_id = create_student()
    course_id = create_course()

    client.post(
        "/enrollments/",
        json={
            "user_id": user_id,
            "course_id": course_id,
            "role": "student"
        }
    )

    response = client.post(
        "/enrollments/",
        json={
            "user_id": user_id,
            "course_id": course_id,
            "role": "student"
        }
    )

    assert response.status_code == 400


def test_get_student_enrollments():
    user_id = create_student()
    course_id = create_course()

    client.post(
        "/enrollments/",
        json={
            "user_id": user_id,
            "course_id": course_id,
            "role": "student"
        }
    )

    response = client.get(f"/enrollments/student/{user_id}")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_admin_get_all_enrollments():
    user_id = create_student()
    course_id = create_course()

    client.post(
        "/enrollments/",
        json={
            "user_id": user_id,
            "course_id": course_id,
            "role": "student"
        }
    )

    response = client.get("/enrollments/?role=admin")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_non_admin_cannot_view_all_enrollments():
    response = client.get("/enrollments/?role=student")

    assert response.status_code == 403


def test_admin_get_course_enrollments():
    user_id = create_student()
    course_id = create_course()

    client.post(
        "/enrollments/",
        json={
            "user_id": user_id,
            "course_id": course_id,
            "role": "student"
        }
    )

    response = client.get(f"/enrollments/course/{course_id}?role=admin")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_student_can_deregister():
    user_id = create_student()
    course_id = create_course()

    client.post(
        "/enrollments/",
        json={
            "user_id": user_id,
            "course_id": course_id,
            "role": "student"
        }
    )

    response = client.request(
        "DELETE",
        "/enrollments/",
        json={
            "user_id": user_id,
            "course_id": course_id,
            "role": "student"
        }
    )

    assert response.status_code == 200


def test_non_student_cannot_deregister():
    user_id = create_student()
    course_id = create_course()

    response = client.delete(
        "/enrollments/",
        json={
            "user_id": user_id,
            "course_id": course_id,
            "role": "admin"
        }
    )

    assert response.status_code == 403
