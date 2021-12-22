from ..data import default_alph


def enc(text: str, alph: str = default_alph, **kwargs) -> str:
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


def dec(text: str, alph: str = default_alph, **kwargs) -> str:
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


def main():
    from ..tests.test import test_crypt

    test_crypt(enc, dec)


if __name__ == "__main__":
    main()
