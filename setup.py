# -*- coding: utf-8 -*-
"""setup."""

from setuptools import setup
from setuptools import find_packages


requires = []
with open('requirements.txt', 'w') as _file:
    _file.write('\n'.join(requires))

setup(
    name='pynacl-demo',
    version='0.0.2',
    url='https://github.com/mtoshi/pynacl-demo',
    author='mtoshi',
    author_email='mtoshi@outlook.com',
    description='Experimental code.',
    packages=find_packages(),
    install_requires=requires,
)
