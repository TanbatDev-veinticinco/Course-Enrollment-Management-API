from fastapi import HTTPException, APIRouter
from app.schemas.schema import CourseCreate, CourseUpdate, CourseResponse
from app.services import course_service


router = APIRouter(
    prefix="/courses",
    tags=["courses"]
)

@router.get("/", response_model=list[CourseResponse])
def get_all_courses():
    courses = course_service.get_all_courses()
    return [course.to_dict() for course in courses]


@router.get("/{course_id}", response_model=CourseResponse)
def get_course(course_id: int):
    course = course_service.get_course_by_id(course_id)
    return course.to_dict()


# ===========Admin only==============

@router.post("/", response_model=CourseResponse, status_code=201)
def create_course(course: CourseCreate, role: str):
    
    if role != "admin":
        raise HTTPException(
            status_code= 403,
            detail= "Only admin can create courses"
        )
    
    new_course = course_service.create_course(
        title=course.title,
        code=course.code
    )

    return new_course.to_dict()


@router.put("/{course_id}", response_model=CourseResponse)
def update_course(course_id: int, course: CourseUpdate, role: str):
     
    if role != "admin":
        raise HTTPException(
            status_code= 403,
            detail= "Only admin can update courses"
        )
    
    updated_course = course_service.update_course(
        course_id=course_id,
        title=course.title,
        code=course.code
    )

    return updated_course.to_dict()


@router.delete("/{course_id}", status_code=204)
def delete_course(course_id: int, role: str):
    if role != "admin":
        raise HTTPException(
            status_code= 403,
            detail= "Only admin can update courses"
        )
    
    course_service.delete_course(course_id)
    return None