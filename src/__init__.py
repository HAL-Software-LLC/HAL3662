"""hal3662 - Web services

Provides
--------
Deployable web services with an eco-conscious billing system.

Documentation
-------------
Documentation is provided primarily by python docstrings. The documentatation is
hosted on GitHub Pages at the following URL: 

Contributing
------------
See: https://github.com/HAL-Software-LLC/HAL3662
"""
import flask as _flask
import logging as _logging
import traceback as _traceback
import unittest as _unittest

app = _flask.Flask(__package__)

@app.route('/', method=['GET', 'POST'])
def index():
  """
  Serve user-provided index file from `static/index.html`.
  """
  return _flask.send_from_directory("static", "index.html")


