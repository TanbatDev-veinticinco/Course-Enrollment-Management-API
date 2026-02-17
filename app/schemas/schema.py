from pydantic import BaseModel, EmailStr, Field
from typing import Literal

#===============User===========

class UserCreate(BaseModel):
    name: str = Field(..., min_length=1, description="Name cannot be empty")
    email: EmailStr
    role : Literal["student", "admin"]


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str


# ==================Course===============
class CourseCreate(BaseModel):
    title: str = Field(..., min_length=1, description="title must not be empty")
    code: str = Field(..., min_length=1, description="code must not be empty")            

class CourseUpdate(BaseModel):
    title: str | None = Field(None, min_length=1)
    code: str | None = Field(None, min_length=1)

class CourseResponse(BaseModel):
    id: int
    title: str
    code: str


# ============Enrollment============

class EnrollmentCreate(BaseModel):
    user_id: int
    course_id: int
    role: Literal["student", "admin"]


class EnrollmentResponse(BaseModel):
    id: int  
    user_id: int  
    course_id: int

class DeregisterRequest(BaseModel):
    user_id: int
    course_id: int 
    role: Literal["student", "admin"]    