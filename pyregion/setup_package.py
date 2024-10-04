from pathlib import Path

from numpy import get_include as get_numpy_include
from setuptools import Extension
from Cython.Build import cythonize

ROOT = Path(__file__).parent.resolve().relative_to(Path.cwd())


def get_extensions():
    _region_filter = Extension(
        name="pyregion._region_filter",
        # define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
        sources=[str(ROOT / "_region_filter.pyx")],
        include_dirs=[get_numpy_include()],
    )

    return cythonize([_region_filter], language_level=3, include_path=["pyregion"])
