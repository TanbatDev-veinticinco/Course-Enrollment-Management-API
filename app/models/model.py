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
        self.title = str
        self.code = str

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "code": self.code
        }
    

class Enrollment:
    def __init__(self, id:int, user_id:int, course_id:int):
        self.id = int
        self.user_id = int 
        self.course_id = int   


    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "course_id": self.course_id
        }   