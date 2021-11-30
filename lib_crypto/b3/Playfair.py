import numpy as np
from ..utils.data import alph
from ..utils.def_str import clear_text

replace_symbol = "ф"


def get_key_matrix(key, alph, cols=8):
    matrix_items = list(key + remove_items_in_str(alph, key))
    matrix = np.array(matrix_items).reshape(-1, cols)

    return matrix


def remove_items_in_str(text, symbols):
    text = list(text)
    for symbol in symbols:
        text.remove(symbol)
    return "".join(text)


def get_bygrams(text):
    bygrams, i = [], 0

    while i <= len(text) - 1:

        block = list(text[i : i + 2])
        i += 2

        if len(block) == 1:
            block.append(replace_symbol)
        if block[0] == block[1]:
            block[1] = replace_symbol
            i -= 1

        bygrams.append("".join(block))

    return bygrams


def get_row(item, matrix):
    return np.argwhere(matrix == item)[0][0]


def get_col(item, matrix):
    return np.argwhere(matrix == item)[0][1]


def check_rows(bygram, matrix):

    if get_row(bygram[0], matrix) == get_row(bygram[1], matrix):
        return True

    return False


def check_cols(bygram, matrix):

    if get_col(bygram[0], matrix) == get_col(bygram[1], matrix):
        return True

    return False


def pleif_row(bygram, matrix, mode="enc"):
    num_cols = matrix.shape[1]
    shift = 1 if mode == "enc" else -1
    return [
        matrix[get_row(item, matrix)][(get_col(item, matrix) + shift) % num_cols]
        for item in bygram
    ]


def pleif_col(bygram, matrix, mode="enc"):
    num_rows = matrix.shape[0]
    shift = 1 if mode == "enc" else -1
    return [
        matrix[(get_row(item, matrix) + shift) % num_rows][get_col(item, matrix)]
        for item in bygram
    ]


def pleif_square(bygram, matrix):

    return [
        matrix[get_row(bygram[0], matrix), get_col(bygram[1], matrix)],
        matrix[get_row(bygram[1], matrix), get_col(bygram[0], matrix)],
    ]


def get_pleif(bygrams, key_matrix, mode="enc"):
    result = []

    for bygram in bygrams:
        new_by = []

        if check_rows(bygram, key_matrix):
            new_by = pleif_row(bygram, key_matrix, mode)

        elif check_cols(bygram, key_matrix):
            new_by = pleif_col(bygram, key_matrix, mode)

        else:
            new_by = pleif_square(bygram, key_matrix)

        result.append("".join(new_by))
    return result


def enc(text, alph=alph, key="штурм"):
    alph = remove_items_in_str(alph, "ё")
    text = clear_text(text.lower(), alph)

    bygrams = get_bygrams(text)
    key_matrix = get_key_matrix(key, alph)

    result = get_pleif(bygrams, key_matrix, "enc")

    return "".join(result)


def dec(text, alph=alph, key="штурм"):
    alph = remove_items_in_str(alph, "ё")
    text = clear_text(text.lower(), alph)

    bygrams = get_bygrams(text)
    key_matrix = get_key_matrix(key, alph)

    result = get_pleif(bygrams, key_matrix, "dec")

    return "".join(result)


def main():
    from ..utils.test import test_crypt

    test_crypt(enc, dec)


if __name__ == "__main__":
    main()
