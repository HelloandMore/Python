@echo off
git add .
git status
git commit -m " orai Python %date%"
git push
echo.
net helpmsg %errorlevel%
timeout 5 /nobreak > nul
exit /b %errorlevel%