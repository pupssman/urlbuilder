Urlbuilder
============


.. image:: https://api.travis-ci.org/pupssman/urlbuilder.svg?branch=master
        :alt: Build Status
        :target: https://travis-ci.org/pupssman/urlbuilder/

.. image:: https://badge.fury.io/py/urlbuilder.svg
        :target: https://badge.fury.io/py/urlbuilder

Simple helper to build URLs in python

Usage example:

.. code:: python

    import requests

    from urlbuilder import URLBuilder

    print requests.get(URLBuilder('http://github.com/').docker.docker.issues[1]).status_code

    # prints 200
