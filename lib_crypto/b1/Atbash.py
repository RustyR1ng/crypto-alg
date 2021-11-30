from ..utils.data import alph


def enc(text, alph=alph, **kwargs):

    return text.translate(
        str.maketrans(alph + alph.upper(), alph[::-1] + alph.upper()[::-1])
    )


def dec(text, alph=alph, **kwargs):

    return text.translate(
        str.maketrans(alph[::-1] + alph.upper()[::-1], alph + alph.upper())
    )


def main():

    from ..utils.test import test_crypt

    test_crypt(enc, dec)


if __name__ == "__main__":
    main()
