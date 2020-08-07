import os

from setuptools import find_packages, setup


def read_requirements():
    """Parse requirements from requirements.txt."""
    reqs_path = os.path.join('.', 'requirements.txt')
    with open(reqs_path, 'r') as f:
        requirements = [line.rstrip() for line in f]
    return requirements


setup(
    name="package",
    version='0.0.1',
    description='sample package',
    packages=find_packages(),
    test_suite="tests",
    install_requires=read_requirements(),
)
