cd /d "%~dp0"
python setup_ubuntu.py -q bdist_wheel --plat-name=manylinux1_x86_64

cd /d "%~dp0"
python setup.py -q bdist_wheel  --plat-name=win_amd64