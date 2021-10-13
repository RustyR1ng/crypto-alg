#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from lib_crypto import get_algs, key_required, get_result
from .utils.forms import EncForm

app = Flask(__name__)

app.jinja_env.add_extension("pypugjs.ext.jinja.PyPugJSExtension")


@app.route("/", methods=["GET", "POST"])
def index():

    form = EncForm(request.form)
    result = ""

    if request.method == "POST":

        alg, text, key, switch = form.get_data()

        result = get_result(text, alg, switch, key)

    return render_template("index.pug", form=form, result=result)


if __name__ == "__main__":
    app.run()
