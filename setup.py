"""
setup.py file for Wild Magic Python extension
"""

# Import native Python modules.
from distutils.core import setup, Extension, Command
import distutils
import inspect
import shutil
import os

# Import user configuration module.
import config

class Clean2(Command):
    """A more thorough clean command."""
    description = 'clean everything generated by a build* command'
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        to_remove = (
            'build',
            'wm5.py',
            'wm5.pyc',
            'wm5_wrap.cpp',
            )
        this_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
        this_dir = os.path.normpath(this_dir)
        for entry in os.listdir(this_dir):
            if entry not in to_remove:
                continue
            entry = os.path.join(this_dir, entry)
            print 'erasing', entry
            if os.path.isfile(entry):
                os.remove(entry)
            elif os.path.isdir(entry):
                shutil.rmtree(entry)

module = Extension(
    name = '_wm5',
    sources = ['wm5.i'],
    swig_opts = [
        '-v',
        '-c++', 
        '-cpperraswarn',
        '-I%s'%config.WM5INCDIR
        ],
    include_dirs = [config.WM5INCDIR],
    extra_compile_args = [
        '-Wno-unused-but-set-variable',
        ],
    library_dirs = [config.WM5LIBDIR],
    libraries = [
        'Wm5Core', 
        'Wm5Mathematics', 
        'Wm5Imagics',
        'Wm5Physics',
        'Wm5GlxGraphics',
        'Wm5GlxApplication',
        'GL',
        ],
    )

setup(
    name         = 'wm5',
    version      = '0.1',
    description  = 'Python wrapper of Geometric Tools\' Wild Magic C++ libraries',
    url          = 'http://python-wild-magic.googlecode.com',
    author       = 'Velimir Mlaker',
    author_email = 'velimir dot mlaker at g mail dot com',
    license      = 'MIT',
    long_description = 
'Python Wild Magic is a Python extension wrapper of Geometric Tools\' Wild Magic -- a collection of C++ libraries for real-time computer graphics and physics, mathematics, geometry, numerical analysis, and image analysis.',
    platforms    = ['Linux',],
    ext_modules  = [module],
    py_modules   = ['wm5'],
    cmdclass     = { 'clean2' : Clean2 },
    )

# The end.
