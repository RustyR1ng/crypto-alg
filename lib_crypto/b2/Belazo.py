from ..utils.data import alph


def create_row(sym, alph):
    row = alph[alph.index(sym) :] + alph[: alph.index(sym)]

    return row


def create_table(key, alph):

    table = [alph]

    for sym in key:

        row = create_row(sym, alph)
        table.append(row)

    return table


def enc(text, alph=alph, key="ильдар", **kwargs):

    result = []
    # table = create_table(alph, key)

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


def dec(text, alph=alph, key="ильдар", **kwargs):

    result = []
    # table = create_table(alph, key)

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


if __name__ == "__main__":

    from ..utils.test import test_crypt

    test_crypt(enc, dec)
