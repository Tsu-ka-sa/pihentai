# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="pihentai",
    version="0.0.1",
    description="nhentai pages from pi's digits",
    license="MIT",
    author="aika",
    packages=find_packages(),
    install_requires=["mpmath"],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
    ]
)
