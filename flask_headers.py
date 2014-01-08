from functools import wraps
from flask import Flask, make_response

def headers(headerDict={}, **headerskwargs):
    '''
    This function is the decorator which is used to wrap a Flask route with. 
    Either pass a dictionary of headers to be set as the headerDict keyword
    argument, or pass header values as keyword arguments. Or, do both :-)
    
    The key and value of items in a dictionary will be converted to strings using
    the `str` method, ensure both keys and values are serializable thusly. 

    :param headerDict: A dictionary of headers to be injected into the response
        headers. Note, the supplied dictionary is first copied then mutated.
    :type origins: dict

    :param headerskwargs: The headers to be injected into the response headers. 
    :type headerskwargs: identical to the `dict` constructor. 
    '''
    _headerDict = headerDict.copy()
    _headerDict.update(headerskwargs)
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            resp = make_response(f(*args, **kwargs))
            h = resp.headers
            for header, value in _headerDict.items():
                h[str(header)] = str(value)
            return resp
        return decorated_function
    return decorator