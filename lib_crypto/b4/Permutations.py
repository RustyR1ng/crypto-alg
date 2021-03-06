import numpy as np

from ..data import default_alph
from ..utils.def_str import clear_text, random_char, to_indexes


def reverse_rows(matrix):
    for i in range(1, matrix.shape[0], 2):
        matrix[i] = np.flip(matrix[i])
    return matrix


def get_text_matrix(text, cols, alph):
    fill = cols - (len(text) % cols) if (len(text) % cols) != 0 else 0
    text = list(text) + ([random_char()] * fill)
    matrix = np.array(text).reshape(-1, cols)

    return reverse_rows(matrix)


def get_key(key, alph=default_alph):

    key = to_indexes(key, alph)
    key = [sorted(key).index(i) for i in key]

    return key


def enc(text, alph=default_alph, key="год"):

    text = clear_text(text, alph)
    cols = len(key)
    text_matrix = get_text_matrix(text, cols, alph)

    key = get_key(key, alph)

    result = ["".join(text_matrix[:, i]) for i in key]
    return "".join(result)


def dec(text, alph=default_alph, key="год"):

    text = clear_text(text, alph)
    cols = len(key)
    rows = len(text) // cols
    text_matrix = get_text_matrix(text, rows, alph).transpose()

    key = get_key(key, alph)

    result = np.empty(text_matrix.shape, dtype=str)

    for i, key_i in enumerate(key):
        result[:, key_i] = (
            text_matrix[:, i] if i % 2 == 0 else np.flip(text_matrix[:, i])
        )
    result = reverse_rows(result)
    result = ["".join(item) for item in result]

    return "".join(result)


def main():
    from ..tests.test import test_crypt

    test_crypt(enc, dec)


if __name__ == "__main__":
    main()
