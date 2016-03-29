from setuptools import setup
# To use a consistent encoding
from codecs import open as open_
from os import path

HERE = path.abspath(path.dirname(__file__))

with open('requirements.txt') as f:
    REQUIRED = f.read().splitlines()

setup(
    name='open-yt-api',
    version='1.0.0',
    description='Open YouTube API library',
    url='https://github.com/Glenpl/open-yt-api',
    download_url = 'https://github.com/Glenpl/open-yt-api/tarball/1.0.0'
    author='Glenpl/Jakub Molinski',
    author_email='kubamolinski@gmail.com',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
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
