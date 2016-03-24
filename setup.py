from setuptools import setup
# To use a consistent encoding
from codecs import open as open_
from os import path

HERE = path.abspath(path.dirname(__file__))

with open_(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

with open('requirements.txt') as f:
    REQUIRED = f.read().splitlines()

setup(
    name='open-yt-api',
    version='0.0.1',
    description='open YouTube API library',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/Glenpl/open-yt-api',
    author='Glenpl/Jakub Molinski',
    author_email='kubamolinski@gmail.com',
    license='MIT',
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='open youtube api',
    packages=['source.youtube'],
    install_requires=REQUIRED,
)

__author__ = 'glenpl'
