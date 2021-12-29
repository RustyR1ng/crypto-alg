from .b1 import *
from .b2 import *
from .b3 import *
from .b4 import *
from .b5 import *
from .b6 import *
from .b7 import *
from .b8 import *
from .b9 import RSA as RSA_ECP
from .b9 import Elgamal as Elgamal_ECP
from .b10 import *


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
    Kuznyechick_ECB = "Kuznyechick ECB"
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
        NAME.Note_Shenon: {
            MODE.ENCRYPT: Note_Shenon.enc,
            MODE.DECRYPT: Note_Shenon.dec,
        },
        NAME.A5_1: {
            MODE.ENCRYPT: A5_1.enc,
            MODE.DECRYPT: A5_1.dec,
        },
        NAME.AES: {
            MODE.ENCRYPT: AES.enc,
            MODE.DECRYPT: AES.dec,
        },
        NAME.Kuznyechick_ECB: {
            MODE.ENCRYPT: Kuznyechik_3413_ECB.enc,
            MODE.DECRYPT: Kuznyechik_3413_ECB.dec,
        },
        NAME.Magma_ECB: {
            MODE.ENCRYPT: Magma_ECB.encrypt_ecb,
            MODE.DECRYPT: Magma_ECB.decrypt_ecb,
        },
        NAME.Elagamal: {
            MODE.ENCRYPT: Elgamal.enc,
            MODE.DECRYPT: Elgamal.dec,
        },
        NAME.Magma_CTR: {
            MODE.ENCRYPT: Magma_CTR.ctr_encrypt,
            MODE.DECRYPT: Magma_CTR.ctr_decrypt,
        },
        NAME.Elgamal_ECP: {
            MODE.ENCRYPT: Elgamal_ECP.enc,
            MODE.DECRYPT: Elgamal_ECP.dec,
        },
        NAME.RSA_ECP: {
            MODE.ENCRYPT: RSA_ECP.enc,
            MODE.DECRYPT: RSA_ECP.dec,
        },
        NAME.GOST_94: {
            MODE.ENCRYPT: GOST_R_34_10_94.enc,
            MODE.DECRYPT: GOST_R_34_10_94.dec,
        },
        NAME.GOST_2012: {
            MODE.ENCRYPT: GOST_R_34_10_2012.enc,
            MODE.DECRYPT: GOST_R_34_10_2012.dec,
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


def get_result(alg, mode, params):
    import inspect

    newparams = {
        key: val
        for key, val in params.items()
        if key in inspect.getfullargspec(get_algs()[alg][mode])[0]
    }
    print(params)
    return get_algs()[alg][mode](**newparams)
