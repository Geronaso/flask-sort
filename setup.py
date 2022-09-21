"""Default setup file for deployment"""

from setuptools import setup

setup(
    name='flask_sort',
    packages=['flask_sort'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
