"""automate.py - hal3662.jasmine.automate module"""

import os as _os
import logging as _logging
import traceback as _traceback
import unittest as _unittest

import flask as _flask
import requests as _requests

_logging.basicConfig(level=_logging.DEBUG)

from .. import app

@app.route('/jasmine/automate', methods=['GET', 'POST'])
def jasmine_automate():
  """
  Drive automation on the jasmine.hal-software.llc system.
  """
  if _flask.request.method == 'GET':
    return _flask.send_from_directory('docs/hal3662/jasmine', 'automate.html')
  return _flask.jsonify(None)

class _Tests(_unittest.TestCase):
  """
  Test the hal3662.jasmine.automate module
  """
  def test_import(self):
    """
    Import the module
    """
    import hal3662.jasmine.automate

  def test_automate_get(self):
    """
    Do an HTTP GET of the /jasmine/automate resource.
    """
    r = _requests.get('http://127.0.0.1:3662/jasmine/automate')
    self.assertEqual(r.status_code, 200)

  def test_automate_post(self):
    """
    Do an HTTP POST of the /jasmine/automate resource.
    """
    j = {'Nick': 'Becker', 'HAL': 8943}
    r = _requests.post('http://127.0.0.1:3662/jasmine/automate', json=j)
    self.assertEqual(r.status_code, 200)
    self.assertEqual(r.json(), None)
