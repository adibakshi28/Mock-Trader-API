# app/services/user_service.py

from typing import Optional, List, Dict
from postgrest import APIError

from app.models.database import supabase


def get_all_users() -> List[Dict]:
    """
    Return all rows from the 'Users' table.
    """
    try:
        response = supabase.table("Users").select("*").execute()
        return response.data or []
    except APIError as e:
        raise e
