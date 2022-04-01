from setuptools import setup, find_packages

setup(
    name='calculator',
    version='0.0.1',
    description='Tdd Calculator',
    author='saamirhye',
    include_package_data=True,
    packages=find_packages(include=['operations'])
)