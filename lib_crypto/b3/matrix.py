import numpy as np
from ..utils.data import alph
from ..utils.def_str import to_indexes


def is_int(num):
    return num % int(num) == 0


def to_slices(items, step):
    return [items[i : i + step] for i in range(0, len(items), step)]


def enc(text, alph=alph, key="кодовое слово же", **kwargs):

    alph += "., ?"

    key_sqrt = np.sqrt(len(key))
    assert is_int(key_sqrt)
    key_sqrt = int(key_sqrt)

    text_indexes = to_indexes(text, alph)
    key_indexes = to_indexes(key, alph)

    text_vectors = [np.array(vec) for vec in to_slices(text_indexes, key_sqrt)]

    if len(text_vectors[-1]) != key_sqrt:

        last_sym = text_vectors[-1][-1]

        text_vectors[-1] = np.append(
            text_vectors[-1],
            np.array([last_sym] * (key_sqrt - len(text_vectors[-1]))),
        )

    text_vectors = [np.asmatrix(vec).T for vec in text_vectors]
    key_mat = np.asmatrix(to_slices(key_indexes, key_sqrt))

    result = [key_mat * vec for vec in text_vectors]
    result = [item.item() for matrix in result for item in matrix]
    result = [alph[item % len(alph)] for item in result]

    return "".join(result)


print(enc("никогда еще штирлиц не был так близок к провалу"))
