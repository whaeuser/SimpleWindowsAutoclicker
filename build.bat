@echo off
REM Build-Skript für SimpleWindowsAutoclicker
REM Erstellt eine ausführbare .exe-Datei mit PyInstaller

echo ========================================
echo SimpleWindowsAutoclicker - EXE Builder
echo ========================================
echo.

REM Prüfe ob Python installiert ist
python --version >nul 2>&1
if errorlevel 1 (
    echo FEHLER: Python ist nicht installiert!
    echo Bitte installieren Sie Python von https://www.python.org/
    pause
    exit /b 1
)

echo [1/4] Python gefunden
echo.

REM Prüfe ob pip installiert ist
pip --version >nul 2>&1
if errorlevel 1 (
    echo FEHLER: pip ist nicht installiert!
    pause
    exit /b 1
)

echo [2/4] Installiere Abhängigkeiten...
pip install -r requirements.txt
if errorlevel 1 (
    echo FEHLER: Konnte Abhängigkeiten nicht installieren!
    pause
    exit /b 1
)
echo.

echo [3/4] Installiere PyInstaller...
pip install pyinstaller
if errorlevel 1 (
    echo FEHLER: Konnte PyInstaller nicht installieren!
    pause
    exit /b 1
)
echo.

echo [4/4] Erstelle EXE-Datei...
pyinstaller --onefile --console --name "SimpleWindowsAutoclicker" autoclicker.py
if errorlevel 1 (
    echo FEHLER: Build fehlgeschlagen!
    pause
    exit /b 1
)
echo.

echo ========================================
echo ✅ BUILD ERFOLGREICH!
echo ========================================
echo.
echo Die EXE-Datei befindet sich in:
echo   dist\SimpleWindowsAutoclicker.exe
echo.
echo Sie können diese Datei jetzt auf jedem Windows-Computer
echo ohne Python-Installation ausführen!
echo.
pause
