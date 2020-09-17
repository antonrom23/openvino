@echo off
cd /d "%~dp0"
python setup.py clean

cd /d "%~dp0"
python setup.py bdist_wheel --plat-name=win_amd64

cd /d "%~dp0"
python setup.py bdist_wheel --plat-name=manylinux1_x86_64

cd /d "%~dp0"
python setup.py bdist_wheel --plat-name=macosx_10_15_x86_64