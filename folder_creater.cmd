@echo off
:loc
echo.
set /p location="Choose the path where you want to create folders > "
echo.

if not exist "%location%" (
    echo The location you've entered is incorrect!
    echo.
    goto :loc
)
pushd %location%

:amount
echo.
set /p amount="Set the number of folders > "
set num=0
echo.

:prog
if num==%amount% (
    goto :exit
) else (
    md Feladat%num%
    set /a num=%num%+1
    goto :prog
)