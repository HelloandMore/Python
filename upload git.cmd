@echo off
git status
git add .
git commit -m Python %date%"
git push
timeout 5 /nobreak > nul
exit /b %errorlevel%