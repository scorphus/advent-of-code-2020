#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from setuptools import find_packages
from setuptools import setup

import os


def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()


tests_require = [
    "autopep8",
    "black",
    "coverage",
    "flake8",
    "ipdb",
    "isort",
    "pytest",
    "pytest-cov",
    "pytest-mock",
    "pre-commit",
]

setup(
    name="aoc",
    version="20",
    url="https://github.com/scorphus/advent-of-code-2020",
    license="BSD-3-Clause",
    description="Advent of Code 2020",
    long_description=read("README.md"),
    classifiers=[
        "License :: OSI Approved :: 3-Clause BSD License License",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    keywords="advent of code",
    author="Pablo S. Blum de Aguiar",
    author_email="scorphus@gmail.com",
    packages=find_packages(),
    install_requires=[],
    extras_require={"tests": tests_require},
    entry_points={"console_scripts": ["aoc = aoc.main:aoc"]},
    include_package_data=True,
    zip_safe=False,
)
