@echo off
REM Install dependencies (Windows)

python3 -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
echo Installation complete. Run run.bat to start the game.
