# -*- coding: utf-8 -*-
from setuptools import setup


short_description = 'flake8 plugin that integrates isort .'

long_description = '{0}\n{1}'.format(
    open('README.rst').read(),
    open('CHANGES.rst').read()
)

setup(
    name='flake8-isort',
    version='2.1.4.dev0',
    description=short_description,
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Flake8',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Quality Assurance',
    ],
    keywords='pep8 flake8 isort imports',
    author='Gil Forcada',
    author_email='gil.gnome@gmail.com',
    url='https://github.com/gforcada/flake8-isort',
    license='GPL version 2',
    py_modules=['flake8_isort', ],
    include_package_data=True,
    test_suite='run_tests',
    zip_safe=False,
    install_requires=[
        'flake8 >= 3.2.1',
        'flake8-polyfill',
        'isort',
        'testfixtures',
    ],
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'flake8.extension': ['I00 = flake8_isort:Flake8Isort', ],
    },
)
