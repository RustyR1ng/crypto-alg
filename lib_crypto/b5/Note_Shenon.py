from ..utils.data import alph
from ..utils.def_str import to_indexes, to_symbols, clear_text
from ..utils.generator import lcg

M = 33
A = 23
C = 357
T0 = 5


def enc(text, alph=alph, **kwargs):
    gamma = [*lcg(M, A, C, T0, len(text))]
    result = [
        (i + j + 1) % M
        for i, j in zip(
            to_indexes(clear_text(text, alph), alph),
            gamma,
        )
    ]

    return result


def dec(text, alph=alph, **kwargs):

    gamma = [*lcg(M, A, C, T0, len(text))]
    result = [
        (i - j - 1) % M
        for i, j in zip(
            text,
            gamma,
        )
    ]
    result = to_symbols(result, alph)

    return result


if __name__ == "__main__":

    from ..utils.test import test_crypt

    test_crypt(enc, dec)
