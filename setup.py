# Copyright (C) 2021  Xueming Zheng
from setuptools import setup

with open("README.md", "r") as fh:
    long_desc = fh.read()

with open('smartpy/version.py') as fv:
    exec(fv.read())

setup(
    name='smartpy',

    version=__version__,

    description='SMARTpy: an open-source rainfall-runoff model in Python',
    long_description=long_desc,
    long_description_content_type="text/markdown",

    url='https://github.com/xp-network/smartpy',

    author='Thibault Hallouin, Eva Mockler, and Michael Bruen',
    author_email='thibault.hallouin@ucdconnect.ie',

    license='GPLv3',

    classifiers=[
        'Natural Language :: English',

        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    packages=['smartpy'],
)
