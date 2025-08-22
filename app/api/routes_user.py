# app/api/routes_user.py
from fastapi import APIRouter, Depends
from app.api.deps import get_current_user

router = APIRouter()

@router.get("/me")
def get_me(user: dict = Depends(get_current_user)):
    return {
        "uid": user["uid"],
        "email": user.get("email"),
        "name": user.get("name", "Anonymous")
    }
