from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='open-yt-api',
    version='0.0.1',
    description='open YouTube API library',
    long_description=long_description,
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
    install_requires=required,
)

_author__ = 'glenpl'
