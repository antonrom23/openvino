import os.path
import sys
from pathlib import Path
from setuptools import setup, find_packages, Extension
from setuptools.command.build_ext import build_ext
from distutils.errors import DistutilsSetupError
from distutils.file_util import copy_file


class PrebuiltExtension(Extension):
    def __init__(self, name, sources, *args, **kw):
        if len(sources) != 1:
            raise DistutilsSetupError(
                "PrebuiltExtension can accept only one source.")
        super(PrebuiltExtension, self).__init__(name, sources, *args, **kw)


class copy_ext(build_ext):
    def run(self):
        for extension in self.extensions:
            if not isinstance(extension, PrebuiltExtension):
                raise DistutilsSetupError(
                    "copy_ext can accept PrebuiltExtension only")
            src = extension.sources[0]
            dst = self.get_ext_fullpath(extension.name)
            copy_file(src, dst, verbose=self.verbose, dry_run=self.dry_run)


def find_prebuilt_extensions(base_dir, ext_pattern):
    extensions = []
    for path in Path(base_dir).glob(ext_pattern):
        relpath = path.relative_to(base_dir)
        if relpath.parent != ".":
            package_names = str(relpath.parent).split(os.path.sep)
        else:
            package_names = []
        package_names.append(path.name.split(".", 1)[0])
        name = ".".join(package_names)
        extensions.append(PrebuiltExtension(name, sources=[str(path)]))
    return extensions


if sys.platform == "linux":
    source_dir = r"sources/lin"
    content_pattern = "**/*.so"
elif sys.platform == "win32":
    source_dir = r"sources/win"
    content_pattern = "**/*.pyd"
else:
    print("Unsupported OS: {}, expected: {}".format(sys.platform, "linux, win32"))
    exit(2)

python_version = "python" + str(sys.version_info.major) + "." + str(sys.version_info.minor)
source_dir = os.path.join(source_dir, python_version)


setup(
    name="openvino_ie4py",
    license="Proprietary - Intel", 
    author="Anton Romanov",
    author_email="anton.romanov@intel.com",
    version="2021.1.1",
    description="OpenVINO Python binding",
    cmdclass={"build_ext": copy_ext},
    ext_modules=find_prebuilt_extensions(source_dir, content_pattern),
    packages=find_packages(source_dir),
    package_dir={"": source_dir},
    zip_safe=False,
    install_requires=[
        "openvino_ie==2021.1.*",
    ],
)
