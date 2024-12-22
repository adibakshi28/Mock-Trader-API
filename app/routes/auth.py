# app/routes/auth.py

from fastapi import APIRouter, HTTPException, status, Request, Depends
from typing import Optional

from app.services.auth_service import register_user, login_user, logout_user
from app.middlewares.jwt_auth import require_active_session

router = APIRouter()

@router.post("/register")
def register(first_name: str, last_name: str, email: str, username: str, password: str):
    """
    If there's a duplicate key (same email/username), supabase raises APIError.
    Our global handler in main.py catches it and returns 400.
    """
    user = register_user(first_name, last_name, email, username, password)
    if not user:
        # Could be some unknown scenario
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Unable to register user."
        )
    return {"message": "User registered successfully", "user_id": user["id"]}

@router.post("/login")
def login(email_or_username: str, password: str, request: Request):
    ip_address: Optional[str] = request.client.host
    token = login_user(email_or_username, password, ip_address=ip_address)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    return {"access_token": token}

@router.post("/logout")
def logout(payload: dict = Depends(require_active_session)):
    """
    Protected route that requires a valid JWT.
    The 'payload' is the decoded token, e.g. {"user_id": 123, "username": "abc"}.
    """
    user_id = payload.get("user_id")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload"
        )
    logout_user(user_id)
    return {"message": "Successfully logged out"}
