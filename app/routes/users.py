# app/routes/users.py

from fastapi import APIRouter, Depends
from typing import List, Dict

from app.middlewares.jwt_auth import require_active_session
from app.services.user_service import get_all_users

router = APIRouter()

@router.get("/all")
def list_all_users(payload: dict = Depends(require_active_session)) -> List[Dict]:
    """
    Returns all registered users
    """
    users = get_all_users()
    return users
