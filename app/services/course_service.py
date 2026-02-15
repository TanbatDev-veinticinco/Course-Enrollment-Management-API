from fastapi import HTTPException
from app.models.model import Course
from app.storage import database


def create_course(title: str, code: str) -> Course:
    for course in database.courses:
        if course.code == code:
            raise HTTPException(
                status_code=400,
                detail=f"Course with code '{code}' already exists"
            )
        
    course_id = database.get_next_course_id()

    new_course = Course(id= course_id, title= title, code=code)

    database.courses.append(new_course) 

    return new_course



def get_all_courses() -> list[Course]:
    return database.courses


def get_course_by_id(course_id: int) -> Course:
    for course in database.courses:
        if course.id == course_id:
            return course
        
    raise HTTPException(
        status_code= 404,
        detail=f"Course with id {course_id} not found"
    )  


def update_course(course_id: int, title: str | None, code: str | None ) -> Course:

    course = get_course_by_id(course_id)


    if code and code != course.code:
        for c in database.courses:
            if c.code == code and c.id != course_id:
                raise HTTPException(
                    status_code=400,
                    detail=f"Course with code '{code}' already exists"
                )


    if title is  not None:
        course.title = title
    if code is not None:
        course.code = code    

    return course



def delete_course(course_id: int) -> None:
    course = get_course_by_id(course_id)

    database.courses.remove(course)



def check_course_exists(course_id: int) -> bool:
    for course in database.courses:
        if course.id == course_id:
            return True
        return False    

