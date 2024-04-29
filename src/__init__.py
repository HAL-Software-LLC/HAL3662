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

@app.route('/', methods=['GET', 'POST'])
def index():
  """
  Serve user-provided index file from `static/index.html`.
  """
  return _flask.send_from_directory("static", "index.html")

@app.route('/<path:path>', methods=['GET', 'POST'])
def files():
  """
  Server user-provided files from `static/<path>`.
  """
  return _flask.send_from_directory("static", path)

class _Tests(_unittest.TestCase):
  """
  Test the hal3662 package.
  """

  def test_import(self):
    """
    Make sure import works okay.
    """
    import hal3662

print("we are moving")
