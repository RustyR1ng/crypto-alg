from ..utils.data import alph


def enc(text, alph=alph, **kwargs):

    result = []

    for i, sym in enumerate(text):

        if sym not in alph:
            result.append(sym)
            continue

        n = len(alph)
        index_alph = alph.index(sym)

        shift = (index_alph + i) % n

        result.append(alph[shift])

    return "".join(result)


def dec(text, alph=alph, **kwargs):

    result = []

    for i, sym in enumerate(text):

        if sym not in alph:
            result.append(sym)
            continue

        n = len(alph)
        index_alph = alph.index(sym)

        shift = (index_alph - i) % n

        result.append(alph[shift])

    return "".join(result)


if __name__ == "__main__":

    from ..utils.test import test_crypt

    test_crypt(enc, dec)
