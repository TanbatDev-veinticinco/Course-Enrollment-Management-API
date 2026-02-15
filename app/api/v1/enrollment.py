from fastapi import APIRouter, HTTPException
from app.schemas.schema import EnrollmentCreate, EnrollmentResponse, DeregisterRequest
from app.services import enrollment_service


router = APIRouter(
    prefix="/enrollments",
    tags=["enrollments"]
)

@router.post("/", response_model=EnrollmentResponse, status_code=201)
def enroll_student(enrollment: EnrollmentCreate):
    new_enrollment = enrollment_service.enroll_student(
        user_id=enrollment.user_id,
        course_id=enrollment.course_id,
        role=enrollment.role
    )

    return new_enrollment.to_dict()


@router.delete("/", status_code=200)
def deregister_student(request: DeregisterRequest):
    result = enrollment_service.deregister_student(
        user_id=request.user_id,
        course_id=request.course_id,
        role=request.role
    )

    return result


@router.get("/student/{user_id}", response_model=list[EnrollmentResponse])
def get_student_enrollments(user_id: int):
    
    enrollments = enrollment_service.get_student_enrollments(user_id)
    return [enrollment.to_dict() for enrollment in enrollments]


#===========admin routes================
@router.get("/", response_model=list[EnrollmentResponse])
def get_all_enrollments(role: str):
    if role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Only admin can view all enrollments"
        )
    
    enrollments = enrollment_service.get_all_enrollments()
    return [enrollment.to_dict() for enrollment in enrollments]

@router.get("/course/{course_id}", response_model=list[EnrollmentResponse])
def get_course_enrollments(course_id: int, role: str):
    if role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Only admin can view course enrollments"
        )
    
    enrollments = enrollment_service.get_course_enrollments(course_id)
    return [enrollment.to_dict() for enrollment in enrollments]