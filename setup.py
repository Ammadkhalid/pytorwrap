from setuptools import setup, find_packages

setup(
name = 'pytorwrap',
version = '1.0',
author = 'Ammad Khalid',
description = 'PytorWrap Module used to apply tor as proxy and renew IP.',
install_requires = ['PySocks >= 1.6.8', 'requests >= 2.9.1', 'stem >= 1.6.0'],
packages = find_packages(),
)
