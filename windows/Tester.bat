@echo off
setlocal
cd /d "%~dp0"
if not exist "GreenBall\GreenBall.exe" goto absent
"GreenBall\GreenBall.exe"
if not errorlevel 1 exit /b 0
echo Le jeu a rencontre une erreur. Consultez le message ci-dessus.
pause
exit /b 1
:absent
echo Extrayez tout le ZIP avant de lancer Tester.bat.
pause
exit /b 1
