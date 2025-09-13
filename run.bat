@echo off
REM Run the moddable snake game (Windows)

IF EXIST venv (
    call venv\Scripts\activate
)

python3 main.py
