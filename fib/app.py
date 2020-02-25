# -*- coding: utf-8 -*-
"""
Author: Amir Mofakhar <amir@mofakhar.info>

Python Version: 3.7
"""
import sys
import logging

from flask import Flask


_LOG = logging.getLogger()

LOG_FORMATTER = logging.Formatter(
    "[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S +0000"
)


class App(object):  # pragma: no cover
    api = None

    @classmethod
    def init_flask(cls):
        cls.api = Flask(__name__)
        cls.init_logger()

    @classmethod
    def init_logger(cls):
        log_level = logging.DEBUG
        root = logging.getLogger()
        root.setLevel(log_level)
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(log_level)
        ch.setFormatter(LOG_FORMATTER)
        root.addHandler(ch)
