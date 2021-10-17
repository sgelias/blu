#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys

try:
    from setuptools import find_packages, setup
except ImportError:
    sys.exit(
        "We need the Python library setuptools to be installed. "
        "Try runnning: python -m ensurepip"
    )


with open("README.md", "r") as readme_file:
    README = readme_file.read()


with open("requirements.txt", "r") as requirements_file:
    REQUIRES = requirements_file.read().splitlines()


SETUP_ARGS = dict(
    author="Neoprospecta DEV's Team 2021.",
    author_email="samuel.elias@neoprospecta.com",
    name="NopCLI",
    version="2.0.0",
    description="Neoprospecta Operational Command Line Interface - NOP-CLI",
    long_description=README,
    long_description_content_type="text/markdown",
    keywords=["Genbank", "Blast", "Neoprospecta", "Operational", "Bioinformatics"],
    url="https://bitbucket.org/neoprospecta/nop_cli/src/main/",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    options={"bdist_wheel": {"universal": True}},
    entry_points={
        "console_scripts": ["nop=app.main:main"],
    },
)


if __name__ == "__main__":
    setup(install_requires=REQUIRES, **SETUP_ARGS)
