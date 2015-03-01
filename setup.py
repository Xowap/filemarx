#!/usr/bin/env python3
# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :

from os import chdir, pardir
from os.path import join, dirname, normpath, abspath
from setuptools import setup


with open(join(dirname(__file__), 'README.rst'), encoding='utf-8') as f:
    readme = f.read()

chdir(normpath(join(abspath(__file__), pardir)))

setup(
    name='filemarx',
    version='0.1.0',
    packages=[],
    scripts=['bin/filemarx'],
    license='WTFPL',
    description='Validate a directory structure using JSON schemas',
    long_description=readme,
    url='https://github.com/Xowap/filemarx',
    author='Rémy Sanchez',
    author_email='remy.sanchez@activkonnect.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: Information Technology',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: System :: Filesystems',
        'Topic :: Utilities',
    ]
)
