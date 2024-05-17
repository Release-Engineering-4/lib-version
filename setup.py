from setuptools import setup

setup(
    name='lib-version',
    version='0.0.1',
    description='A simple library to get the version of the library',
    url='https://github.com/Release-Engineering-4/lib-version',
    author='Release Engineering 4',
    author_email='m.d.yang@student.tudelft.nl',
    packages=['libversion'],
    package_data={
        "":["*.txt"]
    },

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Students',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ]
)