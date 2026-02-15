from fastapi import FastAPI
from app.api.v1 import user, course, enrollment


app = FastAPI(
    title="Course Enrollment Management API",
    description="API for managing course enrollments, allowing users to create accounts, view courses, and enroll in courses.",
)

app.include_router(user.router)
app.include_router(course.router)
app.include_router(enrollment.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Course Enrollment Management API!"}