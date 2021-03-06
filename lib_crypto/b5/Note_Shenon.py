from ..data import default_alph
from ..utils.def_str import clear_text, to_indexes, to_symbols
from ..utils.generator import lcg

M = 33
A = 23
C = 357
T0 = 5


def enc(text: str, alph: str = default_alph, **kwargs) -> str:
    gamma = [*lcg(M, A, C, T0, len(text))]
    result = [
        (i + j + 1) % M
        for i, j in zip(
            to_indexes(clear_text(text, alph), alph),
            gamma,
        )
    ]

    return f"M={M},A={A},C={C},T0={T0}" + " ".join(map(str, result))


def dec(text: str, alph: str = default_alph, **kwargs):
    text = list(map(int, text.split(" ")))
    gamma = [*lcg(M, A, C, T0, len(text))]
    result = [
        (i - j - 1) % M
        for i, j in zip(
            text,
            gamma,
        )
    ]
    result = to_symbols(result, alph)

    return  f"M={M},A={A},C={C},T0={T0}" + result


def main():
    from ..tests.test import test_crypt

    test_crypt(enc, dec)


if __name__ == "__main__":
    main()
