from Cython.Build import cythonize
from setuptools import Extension, setup
import multidict

# to compile run
# python tools/setup_cython_test.py build_ext --inplace
# NOTE: do not run in the tools directory directly

if __name__ == "__main__":
    breakpoint()
    setup(
        ext_modules=cythonize(
            Extension(
                "downstream_cython_consumer", sources=["downstream_cython_consumer.pyx"]
            )
        ),
        include_dirs=[multidict.get_include()],
    )
