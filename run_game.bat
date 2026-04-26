@echo off
REM ================================
REM The Forgotten Crypt - Game Launcher
REM ================================

echo.
echo ====================================
echo   ^^!  THE FORGOTTEN CRYPT  ^^!
echo ====================================
echo.

cd /d "%~dp0"

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.6+ from https://www.python.org/
    pause
    exit /b 1
)

echo Launching adventure game...
echo.

python main.py

if errorlevel 1 (
    echo.
    echo ERROR: Failed to start the game
    pause
)
