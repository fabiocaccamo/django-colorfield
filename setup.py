import os
from distutils.core import setup

version = '0.1.1'

setup(
    name="django-colorfield",
    version=version,
    keywords=["django", "color"],
    author='Jared Forsyth',
    author_email='jared@jaredforsyth.com',
    license='MIT',
    long_description="A small app providing a colorpicker field for django",
    description="A small app providing a colorpicker field for django",
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
    packages=['colorfield'],
    install_requires=['django>=1.2'],
    requires=['django (>=1.2)'],
)

