
@echo off
REM Build Python app into EXE using PyInstaller
pyinstaller --noconfirm --onefile --windowed --icon=app_icon.ico worldcapitals.spec
pause
