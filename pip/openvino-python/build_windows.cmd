@echo off

set python35 = C:\Users\antonrom\AppData\Local\Programs\Python\Python35\python.exe


cd /d "%~dp0"
python setup.py bdist_wheel --plat-name=win_amd64