from setuptools import setup, find_packages

VERSION = '0.2.2'
DESCRIPTION = 'SmartPy Python package'
LONG_DESCRIPTION = 'SmartPy Python package'

setup(
    name='smartpy',
    version=VERSION,
    author='Xueming Zheng',
    author_email='rocalex0220@outlook.com',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['smartpy'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
