@echo off

set python36 = C:\Python\3.6\pip\Scripts\python.exe
set python37 = C:\Python\3.7\pip\Scripts\python.exe
set python38 = C:\Python\3.8\pip\Scripts\python.exe

set VERSION=2021.2
set BUILD=165

::cd /d "%~dp0"
::%python36% setup.py bdist_wheel --plat-name=win_amd64 --build=%BUILD%

cd /d "%~dp0"
%python37% setup.py bdist_wheel --plat-name=win_amd64 --build=%BUILD%

::cd /d "%~dp0"
::%python38% setup.py bdist_wheel --plat-name=win_amd64 --build=%BUILD%