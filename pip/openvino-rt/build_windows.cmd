@echo off
cd /d "%~dp0"
python setup.py -q bdist_wheel  --plat-name=win_amd64
