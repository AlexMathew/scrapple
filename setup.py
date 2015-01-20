#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


readme = open('README.md').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = open('requirements.txt').read().split('\n')

test_requirements = ['mock', 'nose']

setup(
    name='scrapple',
    version='0.1.0',
    description='A framework for creating web scrapers',
    long_description=readme + '\n\n' + history,
    author='Alex Mathew',
    author_email='alexmathew003@gmail.com',
    url='https://github.com/scrappleapp/scrapple',
    packages=find_packages(exclude=('tests',)),
    package_dir={'scrapple':
                 'scrapple'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='scrapple',
    entry_points={
        'console_scripts': ['scrapple = scrapple.cmd:runCLI']
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
