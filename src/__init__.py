"""__init__.py - hal3662 package

Provides
--------
Deployable web services with an eco-conscious billing system.

Documentation
-------------
Documentation is provided primarily by python docstrings. The documentatation is
hosted on GitHub: https://hal-software-llc.github.io/HAL3662/

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

_logging.basicConfig(level=_logging.DEBUG)

# create Flask app for the package
app = _flask.Flask(__package__)

# import objects from all modules
from .info import *

@app.route('/', methods=['GET', 'POST'])
def root():
  """
  Return information about the `hal3662` python package.
  """
  if _flask.request.method == 'GET':
    return _flask.send_from_directory('docs', 'hal3662.html')

@app.route('/favicon.ico', methods=['GET', 'POST'])
def favicon():
  """
  Return favicon.ico file for the HAL 3662 system.
  """
  r = _flask.make_response(_ico)
  r.mimetype = "image/ico"
  return r
_ico = _base64.b64decode(b"AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///8A////AP///wD///8AwF4oKsBeKIPAXiiZwF4obsBeKEfAXii3wF4o+sBeKO7AXih4wF4pBP///wD///8A////AP///wDMeVkAwF4oisBeKP/AXij/wF4o/8BeKNHAXij/wF4o/8BeKP/AXijewF4oosBeKCX///8A////AP///wDt29YQ3rqxvMBeKP/AXij/wF4o/8BeKP/AXij/wF4o/8BeKLzAXii+wF4oWsBeKD/AXihzwF4oEP///wC7UB4A/fr5wtSgkf/AXij/wF4o/8BeKP/AXij/wF4o/8BeKP/AXij1wF4oucBeKJvAXihO////AP///wD///8A+vXzYP/////Ni3X/wF4o/8BeKP/AXij/wF4o/8BeKP/AXij/wF4o/8BeKP/AXij6wF4oksBeKC3///8A////ANvb28Hu7u7/zo97/8BeKP/AXij/wF4o/8BeKP/AXij/wF4o/8BeKP/AXij/wF4o/8BeKOPAXiiJwmMzAP///wD8+Pf26urq/8+jlv/AXij/wF4o/8BeKP/AXiidwF4ob8BeKOLAXij/wF4o/8BeKP/AXij/wF4o58BeKLfAXigK///////////e1NH/vVwn/8BeKP/AXiiY////AP///wDAXigfwF4o7cBeKP/AXij/wF4o/8BeKPjAXiiFwF4oDPz49+L//////////8OxrP+yViT/wF4oDv///wD///8A////AMBeKIPAXij/wF4o/8BeKP/AXij3wF4ozcBeKIX79/ac8ePf//Hj4P/+/v3/vb28/wAAAED///8A////AP///wDAXihdwF4o/8BeKP/AXij/wF4o/8BeKM3AXig4AAAAKm4zE/WHQBn/s5GH/7q1s/9aKQ7fAAAASv///wD///8AwF4oP8BeKP/AXij/wF4o/8BeKK/AXijiwF4oa////wCcaFd4wLSx/+Ph4f/mzcf/wF4oN8ZmOAD///8A////AMBeKIHAXij/wF4o/8BeKPTAXiidwF4oH8BeKJy8UwAAwF4o8MBeKOzAXii+wF4oW////wD///8A////AMBeKBbAXijswF4o/8BeKP/AXihvwF4opf///wDAXigdvVYGAMBeKNHAXigU////AP///wD///8A////AMBeKAvAXijCwF4o/8BeKP/AXii+wF4oHsBeKG////8A////AP///wDAXigd////AP///wD///8A////AMBeKDzAXijRwF4o3sBeKODAXijLwF4oHqkAAADAXigK////AP///wD///8A////AP///wD///8A////AMBfKgLAXigzwF4oV8BeKKLAXigdwF4oCv///wD///8A////AP///wD///8A8AMAAOADAACAAQAAgAcAAAADAAAAAwAAAAAAAAMAAAADgAAAA4AAAAGAAACDgAAAhwIAAJ4DAAC8CwAA+B8AAA==")

@app.route('/<path:path>', methods=['GET', 'POST'])
def docs(path):
  """
  Return static HTML from docs directory.
  """
  if _flask.request.method == 'GET':
    return _flask.send_from_directory('docs', path)


class _Tests(_unittest.TestCase):
  """
  Test the hal3662 package
  """
  def test_import(self):
    """
    Import the package
    """
    import hal3662
