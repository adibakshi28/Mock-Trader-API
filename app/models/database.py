# app/models/database.py

import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")  
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY") 

supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

def check_connection() -> bool:
    """
    Attempt a simple query to confirm DB connectivity.
    If it fails, we'll return False; else True.
    """
    try:
        response = supabase.table("Users").select("*").limit(1).execute()
        return True
    except Exception:
        return False
