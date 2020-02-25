# -*- coding: utf-8 -*-
"""
Author: Amir Mofakhar <amir@mofakhar.info>

Python Version: 3.7
"""
from os import environ


# it starts to return from the first Fibonacci item after reaching this limit.
MAXIMUM_FIB_LENGTH = int(environ.get("MAXIMUM_FIB_LENGTH", 100))
