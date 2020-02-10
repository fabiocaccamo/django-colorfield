from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.md") as history_file:
    history = history_file.read()

version = '0.1.17'

setup(
    name='django-colorfield',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    version=version,
    description='A small app providing a colorpicker field for django',
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    author='Jared Forsyth',
    author_email='jared@jaredforsyth.com',
    url='https://github.com/jaredly/django-colorfield',
    download_url='https://github.com/jaredly/django-colorfield/archive/%s.tar.gz' % version,
    keywords=['django', 'color', 'field', 'admin'],
    requires=['django (>=1.2)'],
    classifiers=['License :: OSI Approved :: MIT License']
)
