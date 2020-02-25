# -*- coding: utf-8 -*-
"""

Author: Amir Mofakhar <amir@mofakhar.info>

Python Version: 3.7
"""
from random import randint

from unittest import TestCase

from fib.utils.math import fibonacci
from fib import settings


def get_fib_item(n):
    phi = (5 ** (1 / 2.0) + 1) / 2
    phi_1 = (5 ** (1 / 2.0) - 1) / -2

    fib_n = ((phi ** n) - (phi_1 ** n)) / (5 ** (1 / 2.0))
    return round(fib_n)


class MathTestCase(TestCase):
    def test_fibonacci_method(self):
        """Testing if fibonacci generator returns correct value"""

        settings.MAXIMUM_FIB_LENGTH = randint(4, 50)
        n = randint(0, settings.MAXIMUM_FIB_LENGTH - 1)
        test_generator = fibonacci()
        item_n = get_fib_item(n)

        for _ in range(n + 1):
            actual_fib = next(test_generator)

        self.assertEqual(item_n, actual_fib)

    def test_reset_after_reaching_the_limit(self):
        """Testing if limit setting works correctly and after that generator
        starts from the begining. We call generator 4 times after resetting to be sure if it
        returns fibonacci item number 4 (0, 1, 1, 2) """
        test_generator = fibonacci()
        settings.MAXIMUM_FIB_LENGTH = randint(4, 100)
        for _ in range(settings.MAXIMUM_FIB_LENGTH):
            next(test_generator)

        for _ in range(4):
            actual_fib = next(test_generator)

        self.assertEqual(2, actual_fib)

    def test_limit_settings_less_than_4(self):
        """Testing if limit setting works correctly for values less than 4"""
        settings_list = [1, 2, 3]
        for set_value in settings_list:
            settings.MAXIMUM_FIB_LENGTH = set_value
            test_generator = fibonacci()
            for _ in range(settings.MAXIMUM_FIB_LENGTH):
                next(test_generator)

            actual_fib = next(test_generator)
            self.assertEqual(0, actual_fib)
