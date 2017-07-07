Urlbuilder
============
Simple helper to build URLs in python

Usage example:

.. code:: python

    import requests

    from urlbuilder import URLBuilder

    print requests.get(URLBuilder('http://github.com/').docker.docker.issues[1]).status_code

    # prints 200
