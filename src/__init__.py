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

_logging.basicConfig(level=_logging.INFO)

# create Flask app for the package
app = _flask.Flask(__package__)

# finish constructing the package
#import hal3662.auth
#import hal3662.billing
#import hal3662.calculate
import hal3662.environ

@app.route('/', methods=['GET', 'POST'])
def root():
  """
  Return information about the `hal3662` python package.
  """
  return _flask.send_from_directory('docs', 'index.html')

@app.route('/favicon.ico', methods=['GET', 'POST'])
def favicon():
  """
  Return favicon.ico file for the HAL 3662 system.
  """
  r = _flask.make_response(_ico)
  r.mimetype = "image/ico"
  return r

@app.route('/<path:path>', methods=['GET', 'POST'])
def docs(path):
  """
  Return static HTML from the docs directory.
  """
  return _flask.send_from_directory('docs', path)

class _Tests(_unittest.TestCase):
  """
  Test the hal3662 package. Assumes that a flask web server is serving the 
  application locally on port 3662.
  """
  def test_import(self):
    """
    Import the package
    """
    import hal3662

  def test_index_get(self):
    """
    Try to GET the resource at /.
    """
    r = _requests.get('http://127.0.0.1:3662')
    self.assertEqual(r.status_code, 200)
    with open('hal3662/docs/index.html') as f:
      e = f.read()
    self.assertEqual(r.text, e)

  def test_index_post(self):
    """
    Try to POST the resource at /.
    """
    j = {'Nick': 'Becker', 'HAL': 8943}
    r = _requests.post('http://127.0.0.1:3662', json=j)
    self.assertEqual(r.status_code, 200)
    with open('hal3662/docs/index.html') as f:
      e = f.read()
    self.assertEqual(r.text, e)

  def test_favicon_get(self):
    """
    Try to GET the resource at /favicon.ico.
    """
    r = _requests.get('http://127.0.0.1:3662/favicon.ico')
    self.assertEqual(r.status_code, 200)
    self.assertEqual(r.content, _ico)

  def test_favicon_put(self):
    j = {'Nick': 'Becker', 'HAL': 8943}
    r = _requests.post('http://127.0.0.1:3662/favicon.ico', json=j)
    self.assertEqual(r.status_code, 200)
    self.assertEqual(r.content, _ico)

  def test_docs_get(self):
    """
    Try to GET the resource at /hal3662.html
    """
    r = _requests.get('http://127.0.0.1:3662/hal3662.html')
    self.assertEqual(r.status_code, 200)
    with open('hal3662/docs/hal3662.html') as f:
      e = f.read()
    self.assertEqual(r.text, e)

  def test_docs_post(self):
    """
    Try to POST the resource at /hal3662.html.
    """
    j = {'Nick': 'Becker', 'HAL': 8943}
    r = _requests.post('http://127.0.0.1:3662/hal3662.html', json=j)
    self.assertEqual(r.status_code, 200)
    with open('hal3662/docs/hal3662.html') as f:
      e = f.read()
    self.assertEqual(r.text, e)

# favicon.ico file
_ico = _base64.b64decode(b""
  b"AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAAAAAAA"
  b"AAAAAAAAAAAAAAAAAAD///8A////AP///wD///8AwF4oKsBeKIPAXiiZwF4obsBe"
  b"KEfAXii3wF4o+sBeKO7AXih4wF4pBP///wD///8A////AP///wDMeVkAwF4oisBe"
  b"KP/AXij/wF4o/8BeKNHAXij/wF4o/8BeKP/AXijewF4oosBeKCX///8A////AP//"
  b"/wDt29YQ3rqxvMBeKP/AXij/wF4o/8BeKP/AXij/wF4o/8BeKLzAXii+wF4oWsBe"
  b"KD/AXihzwF4oEP///wC7UB4A/fr5wtSgkf/AXij/wF4o/8BeKP/AXij/wF4o/8Be"
  b"KP/AXij1wF4oucBeKJvAXihO////AP///wD///8A+vXzYP/////Ni3X/wF4o/8Be"
  b"KP/AXij/wF4o/8BeKP/AXij/wF4o/8BeKP/AXij6wF4oksBeKC3///8A////ANvb"
  b"28Hu7u7/zo97/8BeKP/AXij/wF4o/8BeKP/AXij/wF4o/8BeKP/AXij/wF4o/8Be"
  b"KOPAXiiJwmMzAP///wD8+Pf26urq/8+jlv/AXij/wF4o/8BeKP/AXiidwF4ob8Be"
  b"KOLAXij/wF4o/8BeKP/AXij/wF4o58BeKLfAXigK///////////e1NH/vVwn/8Be"
  b"KP/AXiiY////AP///wDAXigfwF4o7cBeKP/AXij/wF4o/8BeKPjAXiiFwF4oDPz4"
  b"9+L//////////8OxrP+yViT/wF4oDv///wD///8A////AMBeKIPAXij/wF4o/8Be"
  b"KP/AXij3wF4ozcBeKIX79/ac8ePf//Hj4P/+/v3/vb28/wAAAED///8A////AP//"
  b"/wDAXihdwF4o/8BeKP/AXij/wF4o/8BeKM3AXig4AAAAKm4zE/WHQBn/s5GH/7q1"
  b"s/9aKQ7fAAAASv///wD///8AwF4oP8BeKP/AXij/wF4o/8BeKK/AXijiwF4oa///"
  b"/wCcaFd4wLSx/+Ph4f/mzcf/wF4oN8ZmOAD///8A////AMBeKIHAXij/wF4o/8Be"
  b"KPTAXiidwF4oH8BeKJy8UwAAwF4o8MBeKOzAXii+wF4oW////wD///8A////AMBe"
  b"KBbAXijswF4o/8BeKP/AXihvwF4opf///wDAXigdvVYGAMBeKNHAXigU////AP//"
  b"/wD///8A////AMBeKAvAXijCwF4o/8BeKP/AXii+wF4oHsBeKG////8A////AP//"
  b"/wDAXigd////AP///wD///8A////AMBeKDzAXijRwF4o3sBeKODAXijLwF4oHqkA"
  b"AADAXigK////AP///wD///8A////AP///wD///8A////AMBfKgLAXigzwF4oV8Be"
  b"KKLAXigdwF4oCv///wD///8A////AP///wD///8A8AMAAOADAACAAQAAgAcAAAAD"
  b"AAAAAwAAAAAAAAMAAAADgAAAA4AAAAGAAACDgAAAhwIAAJ4DAAC8CwAA+B8AAA=="
)
