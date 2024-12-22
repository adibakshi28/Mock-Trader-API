# app/utils/exceptions.py

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from postgrest import APIError

def register_exception_handlers(app: FastAPI):
    """
    Attach all global exception handlers to the provided FastAPI 'app'.
    """

    @app.exception_handler(APIError)
    async def supabase_api_error_handler(request: Request, exc: APIError):
        """
        If supabase raises an APIError (duplicate key, invalid query, etc.),
        return a 400 with JSON describing the problem.
        """
        return JSONResponse(
            status_code=400,
            content={"error": "Supabase API Error", "details": str(exc)}
        )

    @app.exception_handler(ValueError)
    async def value_error_handler(request: Request, exc: ValueError):
        """
        Example: If you raise ValueError in your code for validation issues
        that aren't Supabase-specific (e.g., custom validations).
        """
        return JSONResponse(
            status_code=400,
            content={"error": "Validation Error", "details": str(exc)}
        )

    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={
                "error": "Internal Server Error",
                "details": str(exc),
            },
        )
