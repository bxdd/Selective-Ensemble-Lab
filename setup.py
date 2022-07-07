import os
import sys
import numpy

from setuptools import find_packages, setup, Extension

# Package meta-data.
NAME = "selab"
DESCRIPTION = "A Selective-Ensemble Research Laboratory"
REQUIRES_PYTHON = ">=3.6.0"
MAINTAINER = "Xiao-Dong Bi"
MAINTAINER_EMAIL = "bxddream@gmail.com"
VERSION = "0.0.1"


# Detect Cython
try:
    import Cython

    ver = Cython.__version__
    _CYTHON_INSTALLED = ver >= "0.24"
except ImportError:
    _CYTHON_INSTALLED = False

if not _CYTHON_INSTALLED:
    print("Required Cython version >= 0.24 is not detected!")
    print('Please run "pip install --upgrade cython" first.')
    exit(-1)

# What packages are required for this module to be executed?
# `estimator` may depend on other packages. In order to reduce dependencies, it is not written here.
REQUIRED = [
    "numpy>=1.16.0,<1.20.0",
    "scipy>=0.19.1",
    "joblib>=0.11",
    "scikit-learn>=0.23,<0.24",
    "graphviz>=0.20",
]


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

libraries = []
if os.name == "posix":
    libraries.append("m")

extensions = [
    Extension(
        "selab.ensemble.forest.tree._libs._tree",
        ["selab/ensemble/forest/tree/_libs/_tree.pyx"],
        include_dirs=[numpy.get_include()],
        libraries=libraries,
        extra_compile_args=["-O3"],
    ),
    Extension(
        "selab.ensemble.forest.tree._libs._splitter",
        ["selab/ensemble/forest/tree/_libs/_splitter.pyx"],
        include_dirs=[numpy.get_include()],
        libraries=libraries,
        extra_compile_args=["-O3"],
    ),
    Extension(
        "selab.ensemble.forest.tree._libs._criterion",
        ["selab/ensemble/forest/tree/_libs/_criterion.pyx"],
        include_dirs=[numpy.get_include()],
        libraries=libraries,
        extra_compile_args=["-O3"],
    ),
    Extension(
        "selab.ensemble.forest.tree._libs._utils",
        ["selab/ensemble/forest/tree/_libs/_utils.pyx"],
        include_dirs=[numpy.get_include()],
        libraries=libraries,
        extra_compile_args=["-O3"],
    ),
]

if __name__ == "__main__":

    setup(
        name=NAME,
        version=VERSION,
        url="https://github.com/bxdd/Selective-Ensemble-Lab",
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        packages=find_packages(),
        include_package_data=True,
        ext_modules=extensions,
        description=DESCRIPTION,
        long_description=long_description,
        long_description_content_type="text/markdown",
        python_requires=REQUIRES_PYTHON,
        install_requires=REQUIRED,
        classifiers=[
            "Intended Audience :: Science/Research",
            "Intended Audience :: Developers",
            "Programming Language :: Python",
            "Topic :: Software Development",
            "Topic :: Scientific/Engineering",
            "Operating System :: POSIX :: Linux",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
        ],
        setup_requires=["cython"],
    )
