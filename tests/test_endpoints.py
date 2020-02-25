# -*- coding: utf-8 -*-
"""

Author: Amir Mofakhar <amir@mofakhar.info>

Python Version: 3.7
"""

from unittest import TestCase
from fib import api


class EndpointsTestCase(TestCase):
    def setUp(self):
        self.client = api.test_client()
        api.config["TESTING"] = True

    def test_fibonacci_endpoint(self):
        expected_responses = [0, 1, 1, 2, 3, 5]
        for expected_fib_rersponse in expected_responses:
            response = self.client.get("/")
            self.assertEqual(response.status_code, 200)
            received_response = response.data
            self.assertEqual(str(expected_fib_rersponse), received_response.decode())
