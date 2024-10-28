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
    
META_FILE = read(META_PATH)

def find_meta(meta):
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta), META_FILE, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError(f"Unable to find __{meta}__ string.".format(meta=meta))

if __name__ == '__main__':
    setup(
        name='tareas',
        description=find_meta('description'),
        license=find_meta('license'),
        url=find_meta('url'),
        version=find_meta('version'),
        author=find_meta('author'),
        author_email=find_meta('email'),
        long_description=open('README.md').read(),
        packages=find_packages(exclude=['tests']),
        zip_safe=False,
        install_requires=open(REQUIREMENTS_PATH).read().split('\n'),
        classifiers=CLASSIFIERS
    )
