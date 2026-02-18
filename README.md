# Course Enrollment Management API

Simple in-memory REST API for managing users, courses, and enrollments built with FastAPI.

**Description**

- **Project:** Course Enrollment Management API
- **What it does:** Create users, manage courses (admin-only), enroll students in courses, and deregister them. Data is stored in-memory (no external DB).

**Quick Start**

- **Create virtualenv (Windows PowerShell):**

  ```powershell
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  pip install fastapi uvicorn pytest
  ```

- **Run server:**

  ```bash
  uvicorn main:app --reload
  ```

**Run tests**

- Uses `pytest`. Run from repository root:

  ```bash
  pytest
  ```

**Project layout**

- **Main entry:** [main.py](main.py)
- **API routers:** [app/api/v1/user.py](app/api/v1/user.py), [app/api/v1/course.py](app/api/v1/course.py), [app/api/v1/enrollment.py](app/api/v1/enrollment.py)
- **Models:** [app/models/model.py](app/models/model.py)
- **Pydantic schemas:** [app/schemas/schema.py](app/schemas/schema.py)
- **Services (business logic):** [app/services/user_service.py](app/services/user_service.py), [app/services/course_service.py](app/services/course_service.py), [app/services/enrollment_service.py](app/services/enrollment_service.py)
- **In-memory storage:** [app/storage/database.py](app/storage/database.py)

**API Endpoints (summary & examples)**

- **Create user**
  - POST /users/
  - Body: {"name": "John", "email": "john@test.com", "role": "student"}
  - Example curl:

    ```bash
    curl -X POST http://localhost:8000/users/ -H "Content-Type: application/json" -d '{"name":"John","email":"john@test.com","role":"student"}'
    ```

- **List users**
  - GET /users/

- **Create course (admin only)**
  - POST /courses/?role=admin
  - Body: {"title": "Mathematics", "code": "MTH101"}
  - Example curl:

    ```bash
    curl -X POST "http://localhost:8000/courses/?role=admin" -H "Content-Type: application/json" -d '{"title":"Mathematics","code":"MTH101"}'
    ```

- **List courses**
  - GET /courses/

- **Get / Update / Delete course**
  - GET /courses/{course_id}
  - PUT /courses/{course_id}?role=admin
  - DELETE /courses/{course_id}?role=admin

- **Enroll student**
  - POST /enrollments/
  - Body: {"user_id": 1, "course_id": 1, "role": "student"}

  ```bash
  curl -X POST http://localhost:8000/enrollments/ -H "Content-Type: application/json" -d '{"user_id":1,"course_id":1,"role":"student"}'
  ```

- **Deregister student**
  - DELETE /enrollments/ (json body: user_id, course_id, role)

- **Get student's enrollments**
  - GET /enrollments/student/{user_id}

- **Admin: list all enrollments / by course**
  - GET /enrollments/?role=admin
  - GET /enrollments/course/{course_id}?role=admin

**Notes / Implementation details**

- Authorization in this project is simulated via a required `role` query parameter or body field; there is no real authentication.
- Data is stored in-memory in `app/storage/database.py` and reset on process restart.
- Pydantic schemas in `app/schemas/schema.py` validate requests and shape responses.

**Developers**

- To extend: replace the in-memory `database` with a persistence layer (SQL/NoSQL), add authentication, and persist ids appropriately.

If you want, I can also add a `requirements.txt` and a quick example script to seed demo data.
