#!/usr/bin/env python

from distutils.core import setup

with open('README.rst') as readme:
    long_description = readme.read()

setup (
    name='ircreactor',
    version='0',
    description='library for manipulating and reacting to IRC messages as mutable state',
    long_description=long_description,
    author='William Pitcock',
    author_email='nenolod@dereferenced.org',
    url='http://kaniini.dereferenced.org/projects/ircreactor.html',
    packages=['ircreactor'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python :: 3',
        'Topic :: Communications :: Chat',
    ],
)
