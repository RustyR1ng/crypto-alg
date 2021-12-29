from ..data import default_alph
from ..utils.def_str import is_symbols_in
from .Belazo import create_row

DEFAULT_KEY = "л"


def check_key(key: str, alph: str) -> None:
    assert len(key) == 1, "Длина ключа должна быть равна 1"
    assert is_symbols_in(key, alph), "Ключ должен содержать только символы из алфавита"


def enc(text: str, alph: str = default_alph, key: str = DEFAULT_KEY, **kwargs) -> str:
    check_key(key, alph)

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


def dec(text: str, alph: str = default_alph, key: str = DEFAULT_KEY, **kwargs) -> str:
    check_key(key, alph)

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


def main():
    from ..tests.test import test_crypt

    test_crypt(enc, dec)


if __name__ == "__main__":
    main()
