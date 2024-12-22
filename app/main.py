# app/main.py

from fastapi import FastAPI
from app.routes import auth, users
from app.core.exceptions import register_exception_handlers
from app.core.startup import register_startup_events
from app import __version__, __author__

app = FastAPI()

# Register exception handlers
register_exception_handlers(app)

# Register startup events
register_startup_events(app)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/user", tags=["Users"])

@app.get("/")
def root():
    return {
        "message": "Welcome to the Mock Trader API with Supabase",
        "version": __version__,
        "author": __author__,
    }
