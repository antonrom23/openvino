import os
import sys
from pathlib import Path
from setuptools import setup


def find_data_files(src_dir):
    local_base_dir = Path(src_dir)
    data_files = []
    for root, directories, filenames in os.walk(local_base_dir):
        for filename in filenames:
            data_files.append([os.path.relpath(root, local_base_dir), [os.path.join(root, filename)]])
    return list(data_files)


#parsing the arguments to define platform specific variables
for arg in sys.argv[1:]:
    if arg == "--plat-name=manylinux1_x86_64":
        source_dir = r"sources/lin"
    elif arg == "--plat-name=win_amd64":
        source_dir = r"sources/win"
    else:
        source_dir = ''


setup(
    name="openvino_ie",
    license="Proprietary - Intel", 
    author="Anton Romanov",
    author_email="anton.romanov@intel.com",
    version="2021.1.1",
    description="OpenVINO Runtime Libraries",
    zip_safe=False,
    data_files=find_data_files(source_dir),
    install_requires=[
        "openvino-tbb==2020.2.*"
    ],
)
