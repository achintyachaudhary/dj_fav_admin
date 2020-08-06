import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

setup(
    name='trollism1234',
    version='0.11',
    packages=['favorite'],
    package_data={
        "favorite": ["migrations/*.py"],
    },
    description='A line of description',
    long_description=README,
    author='yourname',
    author_email='yourname@example.com',
    url='https://github.com/achintyachaudhary/dj_fav_admin/',
    license='MIT',
    install_requires=[
        'chaudhary',
    ]
)
