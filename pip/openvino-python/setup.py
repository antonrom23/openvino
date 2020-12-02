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


def find_data_files(src_dir):
    local_base_dir = Path(src_dir)
    data_files = []
    for root, directories, filenames in os.walk(local_base_dir):
        for filename in filenames:
            data_files.append([os.path.relpath(root, local_base_dir), [os.path.join(root, filename)]])
    return list(data_files)


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
elif sys.platform == "darwin":
    source_dir = r"sources/macos_10_15"
    content_pattern = "**/*.so"    
else:
    print("Unsupported OS: {}, expected: {}".format(sys.platform, "linux, win32, darwin"))
    exit(2)

python_version = "python" + str(sys.version_info.major) + "." + str(sys.version_info.minor)
runtime_dir = os.path.join(source_dir, "runtime")
binding_dir = os.path.join(source_dir, python_version)

# reading description from README.md
with open("sources/docs/README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    version=os.getenv('VERSION'),
    author_email="openvino_pushbot@intel.com",
    name="openvino",
    license="Proprietary - Intel", 
    author="Intel Corporation",
    description="Inference Engine Python* API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    cmdclass={"build_ext": copy_ext},
    ext_modules=find_prebuilt_extensions(binding_dir, content_pattern),
    packages=find_packages(binding_dir),
    package_dir={"": binding_dir},
    data_files=find_data_files(runtime_dir),
    zip_safe=False,
    install_requires=[
        "tbb>=2020.2.*",
        "numpy>=1.16.3"
    ],
)
