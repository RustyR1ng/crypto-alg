from ..data import default_alph


def enc(text: str, alph: str = default_alph, **kwargs) -> str:
    return text.translate(
        str.maketrans(alph + alph.upper(), alph[::-1] + alph.upper()[::-1])
    )


def dec(text: str, alph: str = default_alph, **kwargs) -> str:
    return text.translate(
        str.maketrans(alph[::-1] + alph.upper()[::-1], alph + alph.upper())
    )


def main():
    from ..tests.test import test_crypt

    test_crypt(enc, dec)


if __name__ == "__main__":
    main()
