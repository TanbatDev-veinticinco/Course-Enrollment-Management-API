from app.models.model import User, Course, Enrollment


users: list[User] = []
courses: list[Course] = []
enrollments: list[Enrollment] = []

user_id_counter = 1
course_id_counter = 1
enrollment_id_counter = 1


def get_next_user_id() -> int:
    global user_id_counter
    current_id = user_id_counter
    user_id_counter += 1
    return current_id


def get_next_course_id() -> int:
    global course_id_counter
    current_id = course_id_counter
    course_id_counter += 1
    return current_id


def get_next_enrollment_id() -> int:
    global enrollment_id_counter
    current_id = enrollment_id_counter
    enrollment_id_counter += 1
    return current_id


def reset_database():
    global users, courses, enrollments
    global user_id_counter, course_id_counter, enrollment_id_counter

    users.clear()
    courses.clear()
    enrollments.clear()

    user_id_counter = 1
    course_id_counter = 1
    enrollment_id_counter = 1
