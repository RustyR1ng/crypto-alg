""" Flask configuration."""

from os import environ, path, urandom


basedir = path.abspath(path.dirname(__file__))
print(basedir)

TESTING = True
DEBUG = True
ENV = "development"
SECRET_KEY = environ.get("SECRET_KEY") or urandom(12)
