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


# parsing the arguments to define platform specific variables
for arg in sys.argv[1:]:
    if arg == "--plat-name=manylinux1_x86_64":
        source_dir = r"sources/lin"
    elif arg == "--plat-name=win_amd64":
        source_dir = r"sources/win"
    elif arg == "--plat-name=macosx_10_15_x86_64":
        source_dir = r"sources/macos_10_15"    
    else:
        source_dir = ''

# reading description from README.md
with open("sources/docs/README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="openvino_ie",
    license="Proprietary - Intel", 
    author="Anton Romanov",
    author_email="anton.romanov@intel.com",
    version="2021.1.081",
    description="OpenVINO™ toolkit",
    long_description_content_type="text/markdown",
    long_description=long_description,
    zip_safe=False,
    data_files=find_data_files(source_dir),
    install_requires=[
        "tbb"
    ],
)
