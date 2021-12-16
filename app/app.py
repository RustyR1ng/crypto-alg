# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from lib_crypto import (
    get_algs,
    key_required,
    get_result,
    alph_required,
    params_required,
    MODE,
)
from flask_cors import CORS
from lib_crypto.utils.data import alph


app = Flask(__name__)
CORS(app)

ALGS = get_algs()


@app.route("/encrypt", methods=["POST"])
def enrypt():
    data = dict(request.form)
    try:
        result = {
            "status": "ok",
            "text": get_result(data["text"], data["alg"], MODE.ENCRYPT),
        }
    except Exception as e:
        result = {
            "status": "error",
            "text": e.__str__(),
        }

    return jsonify(result)


@app.route("/decrypt", methods=["POST"])
def decrypt():
    data = dict(request.form)
    try:
        result = {
            "status": "ok",
            "text": get_result(data["text"], data["alg"], MODE.DECRYPT),
        }
    except Exception as e:
        result = {
            "status": "error",
            "text": e.__str__(),
        }

    return jsonify(result)


@app.route("/algs", methods=["GET"])
def algs():
    data = {
        name: {
            "key": key_required(name),
            "alph": alph_required(name),
            "params": params_required(name),
        }
        for name in ALGS.keys()
    }
    return jsonify(data)


@app.route("/default/alph", methods=["GET"])
def default_alph():
    return alph
