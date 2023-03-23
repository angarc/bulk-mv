#!/usr/bin/env python

from setuptools import find_packages
from setuptools import setup

setup(
    name='bulk-mv',
    version="0.1.2",
    description='Move, rename, delete, and add files as fast as you can use Vim.',
    author='Angel Garcia',
    author_email='angarc37@gmail.com',
    url='https://github.com/angarc/bulk-mv',
    py_modules=[
        'bulk_mv.__main__',
    ],
    packages=find_packages(),
    # install_requires=[
    # ],
    entry_points={'console_scripts': ['bmv = bulk_mv.__main__:main']},
)
