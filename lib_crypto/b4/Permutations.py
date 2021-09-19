import numpy as np
from ..utils.data import alph
from ..utils.def_str import to_indexes, to_symbols, clear_text

text = "пример маршрутной перестановкиа"


def reverse_rows(matrix):
    for i in range(1, matrix.shape[0], 2):
        matrix[i] = np.flip(matrix[i])
    return matrix


def get_text_matrix(text, cols):
    fill = cols - (len(text) % cols) if (len(text) % cols) != 0 else 0
    text = list(text) + ([text[-1]] * fill)
    matrix = np.array(text).reshape(-1, cols)

    return reverse_rows(matrix)


def get_key(key, alph):

    key = to_indexes(key, alph)
    key = [sorted(key).index(i) for i in key]

    return key


def enc(text, alph=alph, key="октябрь", cols=7):
    text = clear_text(text, alph)
    text_matrix = get_text_matrix(text, cols)
    print(text_matrix)

    key = get_key(key, alph)

    result = ["".join(text_matrix[:, i]) for i in key]
    return "".join(result), text_matrix.shape[0]


def dec(text, alph=alph, key="октябрь", rows=4):
    text = clear_text(text, alph)
    text_matrix = get_text_matrix(text, rows).transpose()

    key = get_key(key, alph)

    result = np.empty(text_matrix.shape, dtype=str)

    for i, key_i in enumerate(key):
        result[:, key_i] = (
            text_matrix[:, i] if i % 2 == 0 else np.flip(text_matrix[:, i])
        )
    result = reverse_rows(result)
    result = ["".join(item) for item in result]

    return "".join(result)


if __name__ == "__main__":
    enc_, rows = enc(text)
    print(enc_)
    dec_ = dec(enc_, rows=rows)
    print(dec_)