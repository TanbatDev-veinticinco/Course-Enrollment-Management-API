from fastapi import HTTPException
from app.models.model import Enrollment
from app.services import user_service, course_service
from app.storage import database


def enroll_student(user_id: int, course_id: int, role: str) -> Enrollment:
    if role != "student":
        raise HTTPException(
            status_code=403,
            detail="Only Student can enroll for the courses"
        )
    
    if not user_service.check_user_exists(user_id):
        raise HTTPException(
            status_code=403,
            detail=f"User with id {user_id} not found"
        )

    if not course_service.check_course_exists(course_id):
        raise HTTPException(
            status_code=404,
            detail=f"Course with id {course_id} not found"
        )
    
    
    # check if already exist
    for enrollment in database.enrollments:
        if enrollment.user_id == user_id and enrollment.course_id == course_id:
            raise HTTPException(
                status_code=400,
                detail="student is already enrolled in this course"
            )
        
    # 5. Create the enrollment
    enrollment_id = database.get_next_enrollment_id()
    new_enrollment = Enrollment(
        id=enrollment_id,
        user_id=user_id,
        course_id=course_id
    )


    # 6. Add to our list
    database.enrollments.append(new_enrollment)
    

    # 7. Return it
    return new_enrollment  


def deregister_student(user_id: int, course_id: int, role: str, ) -> dict:

    enrollment_to_remove = None
    for enrollment in database.enrollments:
        if enrollment.user_id == user_id and enrollment.course_id == course_id:
            enrollment_to_remove = enrollment
            break

    if not enrollment_to_remove:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )   
    
    if role == "student":
        pass
    elif role == "admin":
        pass
    else:
        raise HTTPException(
            status_code=403,
            detail="Invalid role"
        )
    

    database.enrollments.remove(enrollment_to_remove)


    return {"message": "student deregister sucessfully"}



def get_student_enrollments(user_id: int) -> list[Enrollment]:
    if not user_service.check_user_exists(user_id):
        raise HTTPException(
            status_code=404,
            detail=f"User with id {user_id} not found"
        )
    

    student_enrollments = [
        enrollment for enrollment in database.enrollments
        if enrollment.user_id == user_id  
    ]

    return student_enrollments


def get_course_enrollments(course_id: int) -> list[Enrollment]:
    if not course_service.check_course_exists(course_id):
        raise HTTPException(
            status_code=404,
            detail=f"course with id {course_id} not found"
        )
    

    course_enrollments = [
        enrollment for enrollment in database.enrollments
        if enrollment.course_id == course_id
    ]

    return course_enrollments


def get_all_enrollments() -> list[Enrollment]:
    return database.enrollments