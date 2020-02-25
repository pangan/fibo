# -*- coding: utf-8 -*-
"""
Author: Amir Mofakhar <amir@mofakhar.info>

Python Version: 3.7
"""
from fib.endpoints import assignment
from fib.app import App

App.init_flask()


# the wsgi api
api = App.api
api.logger_name = "flask.app"  # type: ignore


api.register_blueprint(assignment.bp)  # type: ignore
