from ..utils.data import alph


def alph_shift_func(alph, key=3):

    return "".join([alph[(alph.index(sym) + key) % len(alph)] for sym in alph])


def enc(text, alph=alph, key=3, **kwargs):
    key = int(key)
    alph_shift = alph_shift_func(alph, key)

    return text.translate(
        str.maketrans(alph + alph.upper(), alph_shift + alph_shift.upper())
    )


def dec(text, alph=alph, key=3, **kwargs):
    key = int(key)
    alph_shift = alph_shift_func(alph, key)

    return text.translate(
        str.maketrans(alph_shift + alph_shift.upper(), alph + alph.upper())
    )


def main():

    from ..utils.test import test_crypt

    test_crypt(enc, dec)


if __name__ == "__main__":
    main()
