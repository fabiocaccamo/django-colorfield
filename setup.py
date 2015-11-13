import os
from distutils.core import setup

version = '0.1.8'

setup(
    name='django-colorfield',
    packages=['colorfield'],
    data_files=[
        ('static', [
            'colorfield/jscolor/arrow.gif', 
            'colorfield/jscolor/cross.gif', 
            'colorfield/jscolor/hs.png',
            'colorfield/jscolor/hv.png',
            'colorfield/jscolor/jscolor.js'
        ]),
        ('templates', [
            'colorfield/color.html'
        ])
    ],
    #include_package_data=True,
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