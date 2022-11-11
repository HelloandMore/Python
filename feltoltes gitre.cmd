@echo off
pushd %~0\..
git config --global user.name "HelloandMore"
git config --global user.email "milan.kondor06@gmail.com"
set /p repositlink="Paste here the link of the reposit > "
git remote add origin "%repositlink%"
git branch -M main
git push -u origin main
echo.
pause
exit /b %errorlevel%