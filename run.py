#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os

from app import app
from livereload import Server


if __name__ == "__main__":

    app.config.from_pyfile("config.py")
    app.debug = True
    server = Server(app.wsgi_app)
    server.serve()
