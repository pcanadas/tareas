from setuptools import setup, find_packages
import os
import re
import codecs

NAME = 'tareas'
META_PATH = os.path.join(NAME, '__init__.py')
REQUIREMENTS_PATH = 'requirements.txt'
CLASSIFIERS = [
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
]
HERE = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    with codecs.open(os.path.join(HERE, *parts), 'rb', 'utf-8') as fp:
        return fp.read()    

if __name__ == '__main__':
    setup(
        name='tareas',
        description='A simple task manager',
        license='MIT',
        url='https://github.com/pcanadas/tareas',
        version='0.1.0',
        author='Patricia Cañadas',
        long_description=open('README.md').read(),
        packages=find_packages(exclude=['tests']),
        zip_safe=False,
        install_requires=[ 'SQLAlchemy', 'flask' ],
        classifiers=CLASSIFIERS
    )
