from Cython.Build.Cythonize import cython_compile


class Opts:
    # build = None
    build = True
    build_inplace = True
    compile_time_env = {}
    depfile = False
    directives = {}
    excludes = []
    force = None
    include_dirs = [
        "/home/wk/src/github/aio-libs/multidict/multidict",
        "/home/wk/src/github/aio-libs/multidict/multidict/_multilib",
    ]
    keep_going = None
    language = None
    options = {
        'include_path': [
            "/home/wk/src/github/aio-libs/multidict/multidict",
            "/home/wk/src/github/aio-libs/multidict/multidict/_multilib",
        ],
    }
    parallel = 1
    quiet = False


opts = Opts()

breakpoint()

cython_compile("downstream_cython_consumer.pyx", opts)
