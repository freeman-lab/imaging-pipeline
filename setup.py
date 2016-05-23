#!/usr/bin/env python

from setuptools import setup

version = '1.0.0'

required = open('requirements.txt').read().split('\n')

setup(
    name='imaging-pipeline',
    version=version,
    description='a pipeline for calcium imaging data built out of modular components',
    author='freeman-lab',
    author_email='the.freeman.lab@gmail.com',
    url='https://github.com/freeman-lab/imaging-pipeline',
    packages=['pipeline'],
    install_requires=required,
    long_description='See ' + 'https://github.com/freeman-lab/imaging-pipeline',
    license='MIT'
)
