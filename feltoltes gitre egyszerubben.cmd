@echo off
git status
git add .
git commit -m "Python %date%"
git push
echo.
net helpmsg %errorlevel%
timeout 5 /nobreak > nul
exit /b %errorlevel%