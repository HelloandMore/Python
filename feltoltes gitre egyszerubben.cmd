@echo off
git status
git add .
git commit -m "Python"
git push
echo.
timeout 5 /nobreak > nul
exit /b %errorlevel%