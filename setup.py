#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='py-wikimarkup',
    version='1.0.2',
    packages=find_packages(),
    description='A basic MediaWiki markup parser.',
    long_description=open('README.rst').read(),
    author='David Cramer',
    author_email='dcramer@gmail.com',
    url='http://www.github.com/dcramer/py-wikimarkup/',
    zip_safe=False,
    include_package_data=True,
    install_requires=['bleach==1.4.3'],
    package_data = { '': ['README.rst'] },
)
