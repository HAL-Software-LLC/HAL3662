"""__init__.py - hal3662.jasmine package

Provides
--------
Deployable web services for the jasmine host in the hal-software.llc computing
domain.

Documentation
-------------
Documentation is provided primarily by python docstrings. The documentatation is
hosted on GitHub: https://hal-software-llc.github.io/HAL3662/jasmine

Contributing
------------
See: https://github.com/HAL-Software-LLC/HAL3662
"""
import base64 as _base64
import logging as _logging
import traceback as _traceback
import unittest as _unittest

import flask as _flask
import requests as _requests

# finish constructing the package
from .automate import *

@app.route('/jasmine', methods=['GET', 'POST'])
def jasmine():
  """
  Return information about the `hal3662.jasmine` python package.
  """
  if _flask.request.method == 'GET':
    return _flask.send_from_directory('docs/hal3662', 'jasmine.html')
  return _flask.jsonify(None)

class _Tests(_unittest.TestCase):
  """
  Test the hal3662.jasmine package. Assumes that a flask web server is serving
  the application locally on port 3662.
  """
  def test_import(self):
    """
    Import the package
    """
    import hal3662.jasmine

  def test_jasmine_get(self):
    """
    Try to GET the resource at /jasmine .
    """
    r = _requests.get('http://127.0.0.1:3662/jasmine')
    self.assertEqual(r.status_code, 200)
    with open('hal3662/docs/hal3662/jasmine.html') as f:
      e = f.read()
    self.assertEqual(r.text, e)

  def test_jasmine_post(self):
    """
    Try to POST the resource at /jasmine.
    """
    j = {'Nick': 'Becker', 'HAL': 8943}
    r = _requests.post('http://127.0.0.1:3662/jasmine', json=j)
    self.assertEqual(r.status_code, 200)
    self.assertEqual(r.json(), None)

