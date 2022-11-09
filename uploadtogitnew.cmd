@echo off
pushd %~0\..
git config --global user.name "HelloandMore"
git config --global user.email "milan.kondor06@gmail.com"
git init
git add *
echo.
set /p commitmessage="Type here a short description of the commit > "
git commit -m "%commitmessage%"
git branch –M main
start https://github.com/HelloandMore?tab=repositories
echo.
set /p repositlink="Paste the reposit's link here > "
git remote add origin "%repositlink%"
git push -u origin main
pause
exit /b %errorlevel%