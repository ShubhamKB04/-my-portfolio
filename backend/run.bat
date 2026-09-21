@echo off
echo ====================================================
echo Starting Rakesh Pal's AI Portfolio Backend (FastAPI)
echo ====================================================

:: Ensure Python is in path for current session
set "PATH=%LOCALAPPDATA%\Programs\Python\Python312;%LOCALAPPDATA%\Programs\Python\Python312\Scripts;%PATH%"

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not found!
    echo Please download Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo Python environment detected:
python --version

echo.
echo Checking dependencies...
python -m pip install -r requirements.txt --quiet

echo.
echo ====================================================
echo FastAPI Server starting at: http://127.0.0.1:8000
echo Swagger API Documentation:  http://127.0.0.1:8000/docs
echo Press CTRL+C to stop the server anytime.
echo ====================================================
echo.

python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
pause
