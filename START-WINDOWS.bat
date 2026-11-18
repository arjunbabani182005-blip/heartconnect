@echo off
title HeartConnect
cd /d "%~dp0"
echo.
echo  HeartConnect is starting...
echo  On this computer open:  http://localhost:8000/templates/login.html
echo  On your phone (same Wi-Fi) open  http://YOUR-IPV4:8000/templates/login.html
echo  Your IPv4 address is shown below as "IPv4 Address".
echo.
ipconfig | findstr /i "IPv4"
echo.
start "" http://localhost:8000/templates/login.html
python -m http.server 8000 || py -m http.server 8000
pause
