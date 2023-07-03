#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The setup script."""
import os

from setuptools import setup, find_packages

this_directory = os.path.abspath(os.path.dirname(__file__))

__author__ = """Han Zhichao"""
__email__ = 'superhin@126.com'
__version__ = '0.1.3'

setup_requirements = []
install_requires = [
    'requests',
    'python-slugify',
    'urllib3==1.26.6',
]


def read_file(filename):
    with open(os.path.join(this_directory, filename), encoding='utf-8') as f:
        return f.read()


setup(
    name='python_yapi',
    version=__version__,
    author=__author__,
    author_email=__email__,
    license="MIT license",
    description='python yapi sdk',
    long_description=read_file('README.md'),
    long_description_content_type="text/markdown",
    url='https://github.com/hanzhichao/python-yapi',

    include_package_data=True,
    packages=find_packages(include=['python_yapi']),
    zip_safe=True,
    setup_requires=setup_requirements,
    install_requires=install_requires,
    keywords=['yapi', 'python-yapi', 'pyyapi', 'yapi-client'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
    ],
)
