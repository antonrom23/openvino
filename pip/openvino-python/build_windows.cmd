@echo off

set python35 = C:\Python\3.5\pip\Scripts\python.exe
set python36 = C:\Python\3.6\pip\Scripts\python.exe
set python37 = C:\Python\3.7\pip\Scripts\python.exe

cd /d "%~dp0"
%python35% setup.py bdist_wheel --plat-name=win_amd64

cd /d "%~dp0"
%python36% setup.py bdist_wheel --plat-name=win_amd64

cd /d "%~dp0"
%python37% setup.py bdist_wheel --plat-name=win_amd64
