from setuptools import setup, find_packages
from os.path import join, dirname
import pyKurtuba

setup(
    name='pyKurtuba',
    description='Python api-client for Kurtuba ',
    url='https://github.com/gadzhi/pyKurtuba',
    author='Gadzhibala Pirmagomedov',
    author_email='gadzhibala@protonmail.com',
    version=pyKurtuba.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    include_package_data=True,
    test_suite='tests',
    install_requires=[
        'requests>=2.18.4'
    ]
)