from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Пользователи"]
)

@router.get("/")
def say_smthng(say_what):
    return f"Saying {say_what}"