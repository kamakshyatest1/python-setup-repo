
from setuptools import setup, find_packages

setup(
    name='vulnerable_package',
    version='0.1.0',
    description='A Python package with a vulnerable dependency for testing purposes',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    python_requires='>=3.6, <4',
    install_requires=[
        'requests<2.20.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
