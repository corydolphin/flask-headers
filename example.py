"""
flask-headers example
===================
This is a tiny Flask Application demonstrating flask-headers, makign it simple
to add cross origin support to your flask app!

:copyright: (C) 2013 by Cory Dolphin.
:license:   MIT/X11, see LICENSE for more details.
"""
from flask import Flask, request

try:
  from flask_headers import headers # support local usage without installed package
except:
  from flask.ext.headers import headers # this is how you would normally import

app = Flask(__name__)



@app.route("/")
@headers(foo='bar')
def helloWorld():
    return '''<h1>Hello Flask-Headers!</h1> Checkout my documentation
on <a href="https://github.com/wcdolphin/flask-headers">Github</a>'''

if __name__ == "__main__":
    app.run(debug=True)
