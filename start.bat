@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

REM Check if venv folder exists
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
    
    call venv\Scripts\activate.bat
    
    if exist requirements.txt (
        echo Installing requirements.txt...
        pip install -r requirements.txt
    )
) else (
    echo venv already exists, skipping creation and installation
)

REM Open new CMD window and run afk.py
start "" cmd /k "cd /d "%SCRIPT_DIR%" && "%SCRIPT_DIR%venv\Scripts\activate.bat" && python afk.py"