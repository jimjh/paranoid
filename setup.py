"""A setuptools based setup module.

See: https://github.com/jimjh/paranoid
"""
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='paranoid',
    version='0.1.0',
    description='Pragmatic Contracts for Python',
    long_description=long_description,
    long_description_content_type='text/x-rst; charset=UTF-8',
    url='https://github.com/jimjh/paranoid',
    author='James Lim',
    author_email='jim@jimjh.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='paranoid contracts',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['six', 'wrapt'],
    extras_require={
        'dev': ['check-manifest'],
    },
    project_urls={
        'Bug Reports': 'https://github.com/jimjh/paranoid/issues',
        'Source': 'https://github.com/jimjh/paranoid/',
    },
)
