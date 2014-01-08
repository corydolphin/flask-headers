# flask-headers

flask-headers is a simple extension to Flask allowing you decorate routes
in order to send headers. 

[![Build Status](https://travis-ci.org/wcdolphin/flask-headers.png?branch=master)](https://travis-ci.org/wcdolphin/flask-headers)

## Installation

Install the extension with using pip, or easy_install.
```bash
$ pip install flask-headers
```

## Usage
This extension exposes a simple decorator to decorate flask routes with. Simply
add `@headers(foo=bar)` below a call to Flask's `@app.route(..)` incanation to
add the header `foo` with the value `bar` to all responses from the given route.


### Simple Usage

```python
@app.route("/")
@headers({'Cache-Control':'public, max-age=30'})
def cacheable():
    return '''<h1>Hello Flask-Headers!</h1> Checkout my documentation
on <a href="https://github.com/wcdolphin/flask-headers">Github</a>'''

```

For a full list of options, please see the full [documentation](http://flask-headers.readthedocs.org/en/latest/)


## Tests
A simple set of tests is included in `test.py`. To run, install nose, and simply invoke `nosetests` or run `python test.py` to exercise the tests. 

## Contributing
Questions, comments or improvements? Please create an issue on Github, tweet at me or send me an email.


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/wcdolphin/flask-headers/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

