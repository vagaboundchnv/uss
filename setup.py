from setuptools import setup, find_packages

setup(
    name="uss",
    version="0.0.1",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['setuptools', 'Django==1.6.1'],
)