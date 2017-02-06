# -*- coding:utf-8 -*-

from setuptools import setup
from setuptools import find_packages

VERSION = '0.0.1'

setup(
    name='pyemails',
    description='find the operator by phone',
    long_description='',
    classifiers=[],
    keywords='',
    author='Lawes',
    author_email='haiou_chen@sina.cn',
    url='https://github.com/MrLawes/pyemails',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'email',
    ],
    version=VERSION,
)