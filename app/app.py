# -*- coding: utf-8 -*-
import traceback

from flask import Flask, jsonify, request
from flask_cors import CORS

from lib_crypto import (
    MODE,
    alph_required,
    get_algs,
    get_result,
    key_required,
    params_required,
)
from lib_crypto.data import default_alph as alph

app = Flask(__name__)
CORS(app)

ALGS = get_algs()


@app.route("/encrypt", methods=["POST"])
def enrypt():
    data = {key: val for key, val in dict(request.form).items() if val != ""}

    alg = data["alg"]
    del data["alg"]
    try:
        result = {
            "status": "ok",
            "text": get_result(alg, MODE.ENCRYPT, data),
        }
    except Exception as e:
        print(traceback.format_exc())
        result = {
            "status": "error",
            "text": e.__str__(),
        }

    return jsonify(result)


@app.route("/decrypt", methods=["POST"])
def decrypt():
    data = {key: val for key, val in dict(request.form).items() if val != ""}
    alg = data["alg"]
    del data["alg"]
    try:
        result = {
            "status": "ok",
            "text": get_result(alg, MODE.DECRYPT, data),
        }
    except Exception as e:
        print(traceback.format_exc())
        result = {
            "status": "error",
            "text": e.__str__(),
        }

    return jsonify(result)


@app.route("/algs", methods=["GET"])
def algs():
    import inspect

    data = {}
    for name, val in ALGS.items():
        encrypt_params = inspect.getfullargspec(val[MODE.ENCRYPT])[0]
        print(name)
        encrypt_params.remove("text")

        decrypt_params = inspect.getfullargspec(val[MODE.DECRYPT])[0]
        decrypt_params.remove("text")
        data.update(
            {
                name: {
                    "encrypt_params": encrypt_params,
                    "decrypt_params": decrypt_params,
                }
            }
        )

    return jsonify(data)


@app.route("/default/alph", methods=["GET"])
def default_alph():
    return alph
