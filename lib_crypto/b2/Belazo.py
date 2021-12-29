from typing import List

from ..data import default_alph
from ..utils.def_str import is_symbols_in


def create_row(sym: str, alph: str) -> str:
    row = alph[alph.index(sym) :] + alph[: alph.index(sym)]
    return row


def create_table(key: str, alph: str) -> List[str]:
    table = [alph]

    for sym in key:

        row = create_row(sym, alph)
        table.append(row)

    return table


DEFAULT_KEY = "ильдар"


def check_key(key, alph):
    assert is_symbols_in(key, alph), "Ключ должен содержать только символы из алфавита"


def enc(text: str, alph: str = default_alph, key: str = DEFAULT_KEY, **kwargs) -> str:
    result = []
    # table = create_table(alph, key)
    check_key(key, alph)
    for i, sym in enumerate(text):

        sym = sym.lower()

        if sym not in alph:

            result.append(sym)
            continue

        key_row_index = i % len(key)
        col_index = alph.index(sym)

        row = create_row(key[key_row_index], alph)
        enc_sym = row[col_index]

        result.append(enc_sym)

    return "".join(result)


def dec(text: str, alph: str = default_alph, key: str = DEFAULT_KEY, **kwargs) -> str:
    result = []
    # table = create_table(alph, key)
    check_key(key, alph)
    for i, sym in enumerate(text):
        sym = sym.lower()

        if sym not in alph:
            result.append(sym)
            continue

        key_row_index = i % len(key)
        row = create_row(key[key_row_index], alph)

        col_index = row.index(sym)
        enc_sym = alph[col_index]

        result.append(enc_sym)

    return "".join(result)


def main():
    from ..tests.test import test_crypt

    test_crypt(enc, dec)


if __name__ == "__main__":
    main()
