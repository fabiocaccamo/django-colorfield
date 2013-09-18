import os
from distutils.core import setup

version = '0.1'

setup(
    name="django-colorfield",
    version=version,
    keywords=["django", "color"],
    long_description="A small app providing a colorpicker field for django",
    description="A small app providing a colorpicker field for django",
    license="Apache Software License",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
    ],
    packages=['colorfield'],
    install_requires=['django>=1.2'],
    requires=['django (>=1.2)'],
)

