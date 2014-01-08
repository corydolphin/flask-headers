try:
    import unittest2 as unittest
except ImportError:
    import unittest

from flask import Flask
try:
  from flask_headers import headers # support local usage without installed package
except:
  from flask.ext.headers import headers # this is how you would normally import


class DefaultsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)

        @self.app.route('/')
        @headers(foo='bar')
        def wildcard():
            return 'Welcome!'

    def test_foo_in_headers(self):
        ''' Ensure foo:bar is in the headers!
        '''
        with self.app.test_client() as c:
            result = c.get('/')
            self.assertEqual(result.headers.get('foo'), 'bar')


class DictionaryTestCase(unittest.TestCase):
    _headers_dict = {"foo":"bar", "baz":"qux"}

    def setUp(self):
        self.app = Flask(__name__)

        @self.app.route('/')
        @headers(self._headers_dict)
        def wildcard():
            return 'Welcome!'

    def test_dict_in_headers(self):
        ''' Ensure foo:bar is in the headers!
        '''
        with self.app.test_client() as c:
            result = c.get('/')
            for k,v in self._headers_dict.items():
                self.assertEqual(result.headers.get(str(k)), str(v))

class HybridTestCase(unittest.TestCase):

    _headers_dict = {"foo":"bar", "baz":"qux"}
    _headers_dict_id = id(_headers_dict)
    _headers_dict_copy = dict(_headers_dict)

    def setUp(self):
        self.app = Flask(__name__)

        @self.app.route('/')
        @headers(self._headers_dict, extraParameter='MagicNumberSleven')
        def wildcard():
            return 'Welcome!'

        @self.app.route('/bar')
        def other():
            return 'baz'


    def test_no_mutation(self):
        '''
            Ensure that even a hybrid approach does not mutate the underlying
            dictionary passed into the headers.

            Note: this is probably a silly test case, but I think it is important
            to document sideeffects, so I did.
        '''
        self.assertEqual(self._headers_dict_copy, self._headers_dict)
        self.assertEqual(id(self._headers_dict), self._headers_dict_id)

    def test_dict_in_headers(self):
        '''
            Ensure that the full set of headers are set.
        '''
        with self.app.test_client() as c:
            result = c.get('/')
            for k,v in self._headers_dict.items():
                self.assertEqual(result.headers.get(str(k)), str(v))
            self.assertEqual(result.headers.get('extraParameter'), 'MagicNumberSleven')

    def test_no_headers_different_route(self):
        '''
            Ensure the headers are only injected into the proper route!

            Note: this is simply a sanity check.
        '''
        with self.app.test_client() as c:
            result = c.get('/bar')
            for k,v in self._headers_dict.items():
                self.assertNotEqual(result.headers.get(str(k)), str(v))
            self.assertNotEqual(result.headers.get('extraParameter'), 'MagicNumberSleven')


if __name__ == "__main__":
     unittest.main()
