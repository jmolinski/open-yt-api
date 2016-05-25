from setuptools import setup
from os import path

HERE = path.abspath(path.dirname(__file__))

setup(
    name='openytapi',
    version='1.1.0',
    description='Open YouTube API library',
    url='https://github.com/Glenpl/openytapi',
    download_url='https://github.com/Glenpl/openytapi/tarball/1.1.0',
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
    packages=['youtube'],
    install_requires=['beautifulsoup4', 'requests']
)

__author__ = 'glenpl'
