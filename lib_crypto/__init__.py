from .b1 import *
from .b2 import *
from .b3 import *
from .b4 import *


class MODE:
    ENCRYPT = 0
    DECRYPT = 1


class NAME:
    Atbash = "Attbash"
    Cesar = "Cesar"
    Polibiy = "Polibiy"
    Belazo = "Belazo"
    Tritemi = "Tritemi"
    Vizhiner = "Vizhiner"
    Matrix = "Matrix"
    Playfair = "Playfair"
    Kardano = "Kardano"
    Permutations = "Permutations"
    Note_Shenon = "Note Shenon"
    A5_1 = "A5/1"
    AES = "AES"
    Kuznyechick_ECB = "Kuznyechick"
    Magma_CTR = "Magma CTR"
    Magma_ECB = "Magma ECB"
    ECC = "ECC"
    Elagamal = "Elgamal"
    RSA = "RSA"
    Elgamal_ECP = "Elgamal ECP"
    RSA_ECP = "RSA ECP"
    GOST_94 = "GOST R 34 10 94"
    GOST_2012 = "GOST R 34 10 2012"
    Diffie_Hellman = "Diffie Hellman"


def get_algs():
    algs = {
        NAME.Atbash: {
            MODE.ENCRYPT: Atbash.enc,
            MODE.DECRYPT: Atbash.dec,
        },
        NAME.Cesar: {
            MODE.ENCRYPT: Cesar.enc,
            MODE.DECRYPT: Cesar.dec,
        },
        NAME.Polibiy: {
            MODE.ENCRYPT: Polibiy.enc,
            MODE.DECRYPT: Polibiy.dec,
        },
        NAME.Belazo: {
            MODE.ENCRYPT: Belazo.enc,
            MODE.DECRYPT: Belazo.dec,
        },
        NAME.Tritemi: {
            MODE.ENCRYPT: Tritemi.enc,
            MODE.DECRYPT: Tritemi.dec,
        },
        NAME.Vizhiner: {
            MODE.ENCRYPT: Vizhiner.enc,
            MODE.DECRYPT: Vizhiner.dec,
        },
        NAME.Matrix: {
            MODE.ENCRYPT: Matrix.enc,
            MODE.DECRYPT: Matrix.dec,
        },
        NAME.Playfair: {
            MODE.ENCRYPT: Playfair.enc,
            MODE.DECRYPT: Playfair.dec,
        },
        NAME.Permutations: {
            MODE.ENCRYPT: Permutations.enc,
            MODE.DECRYPT: Permutations.dec,
        },
        NAME.Kardano: {
            MODE.ENCRYPT: Kardano.enc,
            MODE.DECRYPT: Kardano.dec,
        },
    }

    return algs


def key_required(alg):
    return alg in [
        NAME.Cesar,
        NAME.Belazo,
        NAME.Vizhiner,
        NAME.Matrix,
        NAME.Playfair,
        NAME.Permutations,
        NAME.Matrix,
        NAME.Playfair,
        NAME.Kardano,
        NAME.Permutations,
        NAME.Note_Shenon,
    ]


def alph_required(alg):
    return alg in [
        NAME.Atbash,
        NAME.Cesar,
        NAME.Polibiy,
        NAME.Belazo,
        NAME.Tritemi,
        NAME.Vizhiner,
        NAME.Matrix,
        NAME.Playfair,
        NAME.Kardano,
        NAME.Permutations,
        NAME.Note_Shenon,
    ]


def params_required(alg):
    return alg in []


def get_result(
    text,
    alg,
    mode,
    key=None,
):
    return get_algs()[alg][mode](text, key=key)
