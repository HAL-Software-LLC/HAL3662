"""environ.py - hal3662.environ module"""

import os as _os
import logging as _logging
import traceback as _traceback
import unittest as _unittest

import flask as _flask
import requests as _requests

_logging.basicConfig(level=_logging.DEBUG)

from hal3662 import app

@app.route('/environ', methods=['GET', 'POST'])
def environ():
  """
  Return information about the computing environment.
  """
  if _flask.request.method == 'GET':
    return _flask.send_from_directory('docs/hal3662', 'environ.html')
  return _flask.jsonify({'computer': True})

class _Tests(_unittest.TestCase):
  """
  Test the hal3662.environ module
  """
  def test_import(self):
    """
    Import the module
    """
    import hal3662.environ

  def test_environ_get(self):
    """
    Do an HTTP GET of the /environ resource.
    """
    r = _requests.get('http://127.0.0.1:3662/environ')
    self.assertEqual(r.status_code, 200)

  def test_environ_post(self):
    """
    Do an HTTP POST of the /environ resource.
    """
    j = {'Nick': 'Becker', 'HAL': 8943}
    r = _requests.post('http://127.0.0.1:3662/environ', json=j)
    self.assertEqual(r.status_code, 200)
    e = {'computer': True}
    self.assertEqual(r.json(), e)
