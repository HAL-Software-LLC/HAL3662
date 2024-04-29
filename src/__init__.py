"""__init__.py - hal3662 package

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
import logging as _logging
import traceback as _traceback
import unittest as _unittest

import flask as _flask
import requests as _requests

app = _flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  """
  Serve documentation for package.
  """
  return _flask.send_from_directory('../docs', 'hal3662.html')

class _Tests(_unittest.TestCase):
  """
  Test the hal3662 package.
  """
  def test_import(self):
    """
    Make sure import works okay.
    """
    import hal3662

  def test_index(self):
    """
    Try to GET the /index.html page.
    """
    r = _requests.get('http://127.0.0.1:3662')
    self.assertEqual(r.status_code, 200)
    fragment = "Deployable web services with an eco-conscious billing system."
    self.assertIn(fragment, r.text)
