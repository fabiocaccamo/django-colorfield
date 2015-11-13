import os
from distutils.core import setup

version = '0.1.7'

setup(
    name='django-colorfield',
    packages=['colorfield'],
    include_package_data=True,
    license='MIT License',
    version=version,
    description='A small app providing a colorpicker field for django',
    long_description='A small app providing a colorpicker field for django',
    author='Jared Forsyth',
    author_email='jared@jaredforsyth.com',
    url='https://github.com/jaredly/django-colorfield',
    download_url='https://github.com/jaredly/django-colorfield/archive/%s.tar.gz' % version,
    keywords=['django', 'color', 'field', 'admin'],
    requires=['django (>=1.2)'], 
    classifiers=['License :: OSI Approved :: MIT License']
)