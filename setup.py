#!/usr/bin/env python3
from distutils.core import setup
from io import open


def read(filename):
    with open(filename, encoding='utf-8') as file:
        return file.read()


setup(
    name='otter',
    version='0.0.1',
    packages=[''],
    url='https://github.com/MA24th/otter',
    license='GNU GPLv2',
    author='Mustafa Asaad',
    author_email='ma24th@yahoo.com',
    description='Honeypot style tool for detection common network attacks',
    long_description=read('README.rst'),
    long_description_content_type="text/x-rst",
    keywords='otter, honeypot, detection, common network attacks',
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: 3.8',
                 'License :: OSI Approved :: GNU General Public License v2 (GPLv2)']
)
