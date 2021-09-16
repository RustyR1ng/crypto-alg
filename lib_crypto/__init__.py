from .b1 import *
from .b2 import *
from .b3 import *


def get_algs():

    algs = {
        "Attbash": {"enc": Atbash.enc, "dec": Atbash.dec},
        "Cesar": {"enc": Cesar.enc, "dec": Cesar.dec},
        "Polibiy": {"enc": Polibiy.enc, "dec": Polibiy.dec},
        "Belazo": {"enc": Belazo.enc, "dec": Belazo.dec},
        "Tritemi": {"enc": Tritemi.enc, "dec": Tritemi.dec},
        "Vizhiner": {"enc": Vizhiner.enc, "dec": Vizhiner.dec},
        "Matrix": {"enc": Matrix.enc, "dec": Matrix.dec},
    }

    return algs


def key_required(alg):
    return alg in ["Cesar", "Belazo", "Vizhiner", "Matrix"]


def get_result(text, alg, switch="enc", key=None):
    return get_algs()[alg][switch](text, key=key)
