#!/usr/bin/env python
from setuptools import setup
from version import VERSION
from setuptools import find_packages



kwargs = {
    "name": "fib",
    "version": VERSION,
    "description": "fib data backend",
    "author": "Amir Mofakhar",
    "author_email": "amir@mofakhar.info",
    "package_dir": {"": "."},
    "packages": find_packages(exclude=["tests", "tests.*"]),

}

if __name__ == "__main__":
    setup(**kwargs)
