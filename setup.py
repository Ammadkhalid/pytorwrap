from setuptools import setup, find_packages

setup(
name = 'pytorwrap',
version = '1.2',
author = 'Ammad Khalid',
author_email = 'ammadkhalid12@gmail.com',
description = 'PytorWrap Module used to apply tor as proxy and renew IP.',
install_requires = ['PySocks >= 1.6.8', 'requests >= 2.9.1', 'stem >= 1.6.0'],
packages = find_packages(),
url = 'https://github.com/Ammadkhalid/pytorwrap'
)
