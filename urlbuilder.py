import posixpath

from urllib import urlencode


class URLBuilder(object):
    """
    Easy-to-use URL builder

    Doctests:

    >>> URLBuilder('http://ya.ru/').foo[1].bar
    URLBuilder(base='http://ya.ru/foo/1/bar', params={})

    >>> str(URLBuilder('http://ya.ru/').foo[1].path(bar='ololo'))
    'http://ya.ru/foo/1/path?bar=ololo'

    >>> import urlparse as up
    >>> url = str(URLBuilder('http://ya.ru/').foo[1].path(foo='ololo',
    ...                                                   bar='pewpew'))
    >>> up.parse_qs(up.urlsplit(url).query)['foo']
    ['ololo']

    """

    def __init__(self, base, params={}):
        self.base = base
        self.params = params

    def __call__(self, **params):
        return URLBuilder(self.base, dict(self.params, **params))

    def __str__(self):
        result = self.base

        if self.params:
            result += '?'
            result += urlencode(self.params)

        return result

    def __getattr__(self, attr):
        return URLBuilder(posixpath.join(self.base, attr), self.params)

    def __getitem__(self, item):
        return self.__getattr__(str(item))

    def __repr__(self):
        return 'URLBuilder(base=%r, params=%r)' % (self.base, self.params)
