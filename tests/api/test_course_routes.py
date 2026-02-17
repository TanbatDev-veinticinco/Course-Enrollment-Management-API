from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_all_courses_empty():
    response = client.get("/courses/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_course_admin_success():
    response = client.post(
        "/courses/?role=admin",
        json={
            "title": "Mathematics",
            "code": "MTH101"
        }
    )

    assert response.status_code == 201
    data = response.json()

    assert data["title"] == "Mathematics"
    assert data["code"] == "MTH101"
    assert "id" in data


def test_create_course_non_admin_forbidden():
    response = client.post(
        "/courses/?role=student",
        json={
            "title": "Physics",
            "code": "PHY101"
        }
    )

    assert response.status_code == 403
    assert response.json()["detail"] == "Only admin can create courses"

def test_get_course_by_id():
    create = client.post(
        "/courses/?role=admin",
        json={
            "title": "Chemistry",
            "code": "CHM101"
        }
    )

    course_id = create.json()["id"]

    response = client.get(f"/courses/{course_id}")

    assert response.status_code == 200
    assert response.json()["id"] == course_id

def test_get_course_not_found():
    response = client.get("/courses/999")

    assert response.status_code == 404


def test_update_course_admin():
    create = client.post(
        "/courses/?role=admin",
        json={
            "title": "Biology",
            "code": "BIO101"
        }
    )

    course_id = create.json()["id"]

    response = client.put(
        f"/courses/{course_id}?role=admin",
        json={
            "title": "Advanced Biology",
            "code": "BIO201"
        }
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Advanced Biology"


def test_update_course_non_admin():
    create = client.post(
        "/courses/?role=admin",
        json={
            "title": "History",
            "code": "HIS101"
        }
    )

    course_id = create.json()["id"]

    response = client.put(
        f"/courses/{course_id}?role=student",
        json={
            "title": "Modern History",
            "code": "HIS201"
        }
    )

    assert response.status_code == 403


def test_delete_course_admin():
    create = client.post(
        "/courses/?role=admin",
        json={
            "title": "Geography",
            "code": "GEO101"
        }
    )

    course_id = create.json()["id"]

    response = client.delete(f"/courses/{course_id}?role=admin")

    assert response.status_code == 204


def test_delete_course_non_admin():
    create = client.post(
        "/courses/?role=admin",
        json={
            "title": "Art",
            "code": "ART101"
        }
    )

    course_id = create.json()["id"]

    response = client.delete(f"/courses/{course_id}?role=student")

    assert response.status_code == 403
