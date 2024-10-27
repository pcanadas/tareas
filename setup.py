from setuptools import setup, find_packages

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
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
        ]
    )
