from fastapi import APIRouter
from app.services.user_service import create_user, get_all_user, get_user_by_id
from app.schemas.schema import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserResponse, status_code=201)
def create_user_route(user: UserCreate):
    new_user = create_user(
        name=user.name,
        email=user.email,
        role=user.role
    )
    return new_user.to_dict()


@router.get("/", response_model=list[UserResponse])
def get_all_users():
    users = get_all_user()
    return [user.to_dict() for user in users]


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    user = get_user_by_id(user_id)
    return user.to_dict()