# -*- coding: utf-8 -*-
"""  # pragma: no cover

Author: Amir Mofakhar <amir@mofakhar.info>

Python Version: 3.7
"""
from flask import Blueprint, Response

from fib.utils.math import fibonacci

bp = Blueprint("assignment", __name__)

fib_method = fibonacci()


@bp.route("/")
def fib_assignment() -> Response:

    return Response(str(next(fib_method)))
