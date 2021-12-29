from typing import Any, List

import numpy as np

from ..data import default_alph
from ..utils.def_str import clear_text, to_indexes, to_symbols


def is_int(num: int) -> bool:
    return num % int(num) == 0


def to_slices(items: List[Any], step: int) -> List[Any]:
    return [items[i : i + step] for i in range(0, len(items), step)]


def check_key(key: str, alph: str) -> int:
    key_sqrt = np.sqrt(len(key))
    assert is_int(key_sqrt), "Длина ключа должна быть квадратным корнем числа N"

    key_sqrt = int(key_sqrt)
    assert all(
        (symbol in alph for symbol in key)
    ), "Ключ содержит символ не входящий в алфавит"

    try:
        np.linalg.inv(text_to_matrix(key, alph, key_sqrt))
    except:
        raise ValueError("Определитель матрицы должен быть не равен нулю")
    return key_sqrt


def text_to_matrix(text: str, alph: str, cols: int) -> Any:
    text_indexes = to_indexes(text, alph)
    matrix = np.asmatrix(to_slices(text_indexes, cols))

    return matrix


def nums_to_vectors(nums: List[int], cols: int) -> List[Any]:
    vectors = [np.array(vec) for vec in to_slices(nums, cols)]

    if len(vectors[-1]) != cols:
        last_sym = vectors[-1][-1]

        vectors[-1] = np.append(
            vectors[-1],
            np.array([last_sym] * (cols - len(vectors[-1]))),
        )

    vectors = [np.asmatrix(vec).T for vec in vectors]

    return vectors


def enc(text: str, alph: str = default_alph, key: str = "бархатный", **kwargs) -> str:
    text = clear_text(text, alph)
    print(to_symbols([1, 4, 8, 3, 7, 2, 6, 9, 5]))
    print(to_symbols([8, 1, 2, 1, 3, 1]))
    key_sqrt = check_key(key, alph)

    text_indexes = to_indexes(text, alph)
    text_vectors = nums_to_vectors(text_indexes, key_sqrt)

    key_mat = text_to_matrix(key, alph, key_sqrt)
    print(key_mat)

    result = [key_mat * vec for vec in text_vectors]
    result = [item.item() for matrix in result for item in matrix]

    return " ".join([str(item) for item in result])


def dec(text: str, alph: str = default_alph, key: str = "бархатный", **kwargs) -> str:

    if type(text) == str:
        text = [int(num) for num in text.split(" ")]

    key_sqrt = check_key(key, alph)

    inv_key_matrix = np.linalg.inv(text_to_matrix(key, alph, key_sqrt))
    print(inv_key_matrix)

    vectors = nums_to_vectors(text, key_sqrt)

    result = [inv_key_matrix * vec for vec in vectors]
    result = [int(item.item() + 0.5) for matrix in result for item in matrix]
    result = to_symbols(result, alph)

    return result


def main():
    from ..tests.test import test_crypt

    test_crypt(enc, dec)


if __name__ == "__main__":
    main()
