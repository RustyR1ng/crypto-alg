from .Belazo import create_row
from ..utils.data import alph


def enc(text, alph=alph, key="л", **kwargs):

    assert len(key) == 1, "Длина ключа должна быть равна 1"

    # alph += " ,:-."
    result = []
    gamma = [key]

    for sym in text:

        sym = sym.lower()
        if sym not in alph:
            continue
        col_index = alph.index(sym)

        row = create_row(gamma[-1], alph)

        enc_sym = row[col_index]

        gamma.append(enc_sym)
        result.append(enc_sym)

    return "".join(result)


def dec(text, alph=alph, key="л", **kwargs):

    # alph += " ,:-."
    result = []
    gamma = key + text

    for i, sym in enumerate(text):

        sym = sym.lower()

        if sym not in alph:
            continue

        row = create_row(gamma[i], alph)
        col_index = row.index(sym)

        enc_sym = alph[col_index]

        result.append(enc_sym)

    return "".join(result)


if __name__ == "__main__":

    from ..utils.test import test_crypt

    test_crypt(enc, dec)
