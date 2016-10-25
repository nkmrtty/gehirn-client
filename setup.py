import os

from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def requirements(fname):
    return [line.strip()
            for line in open(os.path.join(os.path.dirname(__file__), fname))]

setup(
    name='gehirn-client',
    version='0.0.1',
    author='Tatsuya NAKAMURA',
    author_email='nkmrtty.com@gmail.com',
    description='An API client for Gehirn Web Services',
    license='MIT',
    url='https://github.com/nkmrtty/gehirn-client',
    packages=find_packages(),
    keywords=['gehirn', 'gws', 'api'],
    install_requires=[]
)
