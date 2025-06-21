# tests/fixtures/cython_capsule_consumer/downstream_cython_consumer.pyx
# tests/fixtures/cython_capsule_consumer/check_capsule_access.py

import shutil
import subprocess
from pathlib import Path

import multidict


TESTS_ROOT_PATH = Path(__file__).parent.resolve()


def test_cython_capsule(pytester, tmp_path: Path) -> None:
    tmp_capsule_tests_path = tmp_path / 'cython_capsule_consumer'
    shutil.copytree(
        TESTS_ROOT_PATH / 'fixtures/cython_capsule_consumer',
        tmp_capsule_tests_path,
    )
    subprocess.check_call(
        (
            'cythonize',
            str(tmp_capsule_tests_path / 'downstream_cython_consumer.pyx'),
            # multidict.__path__,
            # include_dirs=[multidict.get_include()],
        ),
        env={'CFLAGS': f'-I{multidict.__path__}'}  # FIXME: shlex
    )
    pytester.run(str(tmp_capsule_tests_path / 'check_capsule_access.py'), '-vvvvv')
