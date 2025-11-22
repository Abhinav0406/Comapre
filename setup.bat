@echo off
REM Setup script for File Compare Tool (Windows)

echo 🚀 Setting up File Compare Tool...

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is required but not installed.
    exit /b 1
)

REM Install Python dependencies
echo 📦 Installing Python dependencies...
pip install -r requirements.txt

REM Check Node.js
where node >nul 2>&1
if errorlevel 1 (
    echo ⚠️  Node.js not found. Electron features will not be available.
    echo    Install Node.js from https://nodejs.org/
) else (
    REM Install Node dependencies
    echo 📦 Installing Node.js dependencies...
    call npm install
)

REM Generate icons if possible
echo 🎨 Generating icons...
pip install cairosvg pillow >nul 2>&1
python generate_icons.py >nul 2>&1
if errorlevel 1 (
    echo ⚠️  Could not generate icons (this is optional)
)

echo ✅ Setup complete!
echo.
echo To run the app:
echo   Web: streamlit run app.py
echo   Electron: npm run electron

pause

