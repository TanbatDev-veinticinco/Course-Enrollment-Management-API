from fastapi import HTTPException
from app.models.model import User
from app.storage import database



def create_user(name: str, email: str, role: str) -> User:
    for user in database.users:
        if user.email == email:
            raise HTTPException(
                status_code=400,
                detail= "Email already exists"
            )
        
    user_id = database.get_next_user_id()

    new_user = User(id=user_id, name=name, email=email, role=role)

    database.users.append(new_user)
    
    return new_user


def get_all_user() -> list[User]:
    return database.users



def get_user_by_id(user_id: int) -> User:
    for user in database.users:
        if user.id == user_id:
            return user
        
    raise HTTPException(
        status_code=404,
        detail=f"user with {user_id} not found"
    )    


def check_user_exists(user_id: int) -> bool:
    for user in database.users:
        if user_id == user_id:
            return True
        return False