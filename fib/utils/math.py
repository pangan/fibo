# -*- coding: utf-8 -*-
"""

Author: Amir Mofakhar <amir@mofakhar.info>

Python Version: 3.7
"""
from typing import Generator

from fib import settings


def fibonacci() -> Generator:
    fib_n = 0
    fib_n_1 = 0
    n = 1
    while True:

        if fib_n == 1:
            if settings.MAXIMUM_FIB_LENGTH == 3:
                fib_n_1 = 0
                fib_n = 0

            n += 1
            yield 1
        elif fib_n == 0:
            if settings.MAXIMUM_FIB_LENGTH != 1:
                fib_n = 1

            n += 1
            yield 0

        fib = fib_n + fib_n_1
        fib_n_1 = fib_n
        fib_n = fib

        if n >= settings.MAXIMUM_FIB_LENGTH:
            fib_n = 0
            fib_n_1 = 0
            n = 0

        n += 1
        yield fib
