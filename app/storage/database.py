from app.models.model import User, Course, Enrollment


users: list[User] = []
course: list[Course] = []
enrollment: list[Enrollment] = []

user_id_counter = 1
course_id_counter = 1
enrollment_id_counter = 1

def get_next_user_id() -> int:
    global user_id_counter
    current_id = user_id_counter
    user_id_counter += 1
    return current_id
