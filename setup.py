#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from distutils.extension import Extension

try:
    from Cython.Distutils import build_ext
    have_cython = True
except ImportError:
    have_cython = False

if have_cython:
    ext_modules = [Extension("pymt5.aes256", ["pymt5/aes256.pyx"]), ]
    cmdclass = {'build_ext': build_ext}
else:
    ext_modules = [Extension("pymt5.aes256", ["pymt5/aes256.c"]), ]
    cmdclass = {}

setup(
    name='pymt5',
    version='0.2.1',
    packages=['pymt5', 'pymt5.structures'],
    ext_modules=ext_modules,
    cmdclass=cmdclass,
    author='gothness',
    author_email='gothness@ymail.com',
    description='Client for MetaTrader 5',
    install_requires=[
        'Cython==0.29.33',
    ],
)
