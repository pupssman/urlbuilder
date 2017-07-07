from os import path
from codecs import open
from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='urlbuilder',
    version='0.1.0',

    description='A simple structural URL builder',
    long_description=long_description,
    url='https://github.com/pupssman/urlbuilder',
    author='Ivan Kalinin',
    author_email='pupssman@yandex-team.ru',
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='URL requests',
    py_modules=["urlbuilder"],
)
