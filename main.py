from fastapi import FastAPI
from app.routes.user import router


app = FastAPI(
    title="Course Enrollment Management API",
    description="API for managing course enrollments, allowing users to create accounts, view courses, and enroll in courses.",
)

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Course Enrollment Management API!"}