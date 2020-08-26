cd /d "%~dp0"
python prepare_linux.py -p 3.5
python setup.py -q bdist_wheel  --python-tag py35   --plat-name=manylinux1_x86_64

cd /d "%~dp0"
python prepare_linux.py -p 3.6
python setup.py -q bdist_wheel  --python-tag py36   --plat-name=manylinux1_x86_64

cd /d "%~dp0"
python prepare_linux.py -p 3.7
python setup.py -q bdist_wheel  --python-tag py37   --plat-name=manylinux1_x86_64

