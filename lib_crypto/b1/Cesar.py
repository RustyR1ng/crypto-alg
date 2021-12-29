from ..data import default_alph
from ..utils.def_str import is_int


def alph_shift_func(alph: str, key: int) -> str:
    return "".join([alph[(alph.index(sym) + key) % len(alph)] for sym in alph])


DEFAULT_KEY = "3"


def enc(text: str, alph: str = default_alph, key: str = DEFAULT_KEY, **kwargs) -> str:
    assert is_int(key), "Введите цифровой ключ"
    key = int(key)
    alph_shift = alph_shift_func(alph, key)

    return text.translate(
        str.maketrans(alph + alph.upper(), alph_shift + alph_shift.upper())
    )


def dec(text: str, alph: str = default_alph, key: str = DEFAULT_KEY, **kwargs) -> str:
    assert is_int(key), "Введите цифровой ключ"
    key = int(key)
    alph_shift = alph_shift_func(alph, key)

    return text.translate(
        str.maketrans(alph_shift + alph_shift.upper(), alph + alph.upper())
    )


def main():
    from ..tests.test import test_crypt

    test_crypt(enc, dec)


if __name__ == "__main__":
    main()
