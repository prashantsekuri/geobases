#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup 
#from distutils.core import setup 

setup(
    name='GeoBases',
    version='0.2',
    author='Alex Prengere',
    author_email='alex.prengere@amadeus.com',
    url='http://mediawiki.orinet.nce.amadeus.net/index.php/GeoBases',
    #license=open('COPYING').read(),
    description='Some Geographical functions.',
    long_description=open('README').read(),
    #data_files = [
    #    ('GeoBases', ['README', 'COPYING', 'setup.py'])
    #],
    #entry_points=("""
    #              [console_scripts]
    #              dates = dates.dates:main
    #              """)
    #packages=find_packages(),
    packages = [
        'GeoBases'
    ],
    #py_modules = [
    #    'SysUtils'
    #],
    install_requires = [
        'python_geohash', 
        'python_Levenshtein', 
        'Flask', 
        'tornado',
        'termcolor',
        'colorama'
    ],
    package_dir = {
        'GeoBases': 'GeoBases'
    },
    package_data = {
        'GeoBases': [
            'DataSources/*/*csv', 
            'DataSources/*/*/*csv'
        ]
    },
    scripts = [
        'Aggregator',
        'GeoBase'
    ]

)
