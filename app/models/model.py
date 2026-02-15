from typing import Literal 

class User:
    def __init__(self, id:int, name:str, email:str, role: Literal["student", "admin"]):
        self.id = id
        self.name = name
        self.email = email
        self.role = role


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "role": self.role
        }    
    


class Course:
    def __init__(self, id:int, title:str, code:str):
        self.id = id
        self.title = title
        self.code = code

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "code": self.code
        }
    

class Enrollment:
    def __init__(self, id:int, user_id:int, course_id:int):
        self.id = id
        self.user_id = user_id
        self.course_id = course_id


    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "course_id": self.course_id
        }   