# app/main.py

from fastapi import FastAPI
from app.routes import auth, users
from app.core.exceptions import register_exception_handlers
from app.core.startup import register_startup_events
from app import __version__, __author__

app = FastAPI()

register_exception_handlers(app)

register_startup_events(app)

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/user", tags=["Users"])

@app.get("/")
def root():
    return {
        "message": "Welcome to the Mock Trader API !",
        "version": __version__,
        "author": __author__,
    }
