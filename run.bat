@echo off

call venv\Scripts\activate

uvicorn app.main:app --reload --host 0.0.0.0 --port 3000

pause
