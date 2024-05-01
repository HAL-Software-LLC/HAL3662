"""info.py - hal3662.info module"""

import logging as _logging
import traceback as _traceback
import unittest as _unittest

import flask as _flask
import requests as _requests

# locate Flask app for the package
from . import app

@app.route('/info', methods=['GET', 'POST'])
def info():
  """
  Return information about the HAL 3662 system.
  """
  if _flask.request.method == 'GET':
    return _flask.send_from_directory('docs/hal3662', 'info.html')

class _Tests(_unittest.TestCase):
  """
  Test the hal3662.info module
  """
  def test_import(self):
    """
    Import the module
    """
    import hal3662.info

  def test_get(self):
    """
    Do an HTTP GET of the /info function.
    """
    r = _requests.get('http://127.0.0.1:3662/info')
    self.assertEqual(r.status_code, 200)
    for f in __doc__.split('\n'):
      if len(strip(f)) > 0:
        _logging.debug(f)
        self.assertIn(f, r.text)
