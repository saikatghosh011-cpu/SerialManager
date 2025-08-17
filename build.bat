@echo off
SETLOCAL

echo === Setting up and building Serial Manager ===
python --version
IF %ERRORLEVEL% NEQ 0 (
  echo Python is not available. Please install Python from https://www.python.org/downloads/windows/ and try again.
  pause
  EXIT /B 1
)

echo.
echo Installing/Upgrading pip & dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

IF %ERRORLEVEL% NEQ 0 (
  echo Failed to install dependencies.
  pause
  EXIT /B 1
)

echo.
echo Building EXE with PyInstaller...
pyinstaller --noconsole --onefile --name SerialManager serial_manager.py

IF %ERRORLEVEL% NEQ 0 (
  echo Build failed.
  pause
  EXIT /B 1
)

echo.
echo Build complete! Find SerialManager.exe inside the "dist" folder.
pause
ENDLOCAL
