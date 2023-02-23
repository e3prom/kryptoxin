# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
requirements = []
with open('requirements.txt', 'r') as fh:
    for line in fh:
        requirements.append(line.strip())

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name="Kryptoxin",
    version="0.9.2",
    description="A security-oriented payload encryption tool written in Python.",
    author="Nicolas Chabbey",
    author_email="eprom@toor.si",
    url="https://github.com/e3prom/kryptoxin",
    readme=readme,
    license=license,
    packages=find_packages(exclude=("tests", "docs")),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Topic :: Security",
    ],
    python_requires=">=3.6",
    install_requires=requirements
)
