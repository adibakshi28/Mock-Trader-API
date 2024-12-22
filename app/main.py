from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app import __version__

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/")
def read_root():
    return {"message": "Hello, World!", "version": __version__}
