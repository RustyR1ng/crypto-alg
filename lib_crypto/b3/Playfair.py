from typing import List

import numpy as np

from ..data import default_alph
from ..utils.def_str import clear_text

REPLACE_SYMBOL = "ф"


class MODE:
    ENCRYPT = 0
    DECRYPT = 1


def get_key_matrix(key: str, alph: str, cols: int = 8) -> np.ndarray:
    matrix_items = list(key + remove_items_in_str(alph, key))
    matrix = np.array(matrix_items).reshape(-1, cols)

    return matrix


def remove_items_in_str(text: str, symbols: str) -> str:
    text = list(text)
    for symbol in symbols:
        text.remove(symbol)
    return "".join(text)


def get_bygrams(text: str) -> List[str]:
    bygrams, i = [], 0

    while i <= len(text) - 1:

        block = list(text[i : i + 2])
        i += 2

        if len(block) == 1:
            block.append(REPLACE_SYMBOL)
        if block[0] == block[1]:
            block[1] = REPLACE_SYMBOL
            i -= 1

        bygrams.append("".join(block))

    return bygrams


def get_row(item: str, matrix: np.ndarray) -> np.ndarray:
    return np.argwhere(matrix == item)[0][0]


def get_col(item: str, matrix: np.ndarray) -> np.ndarray:
    return np.argwhere(matrix == item)[0][1]


def check_rows(bygram: str, matrix: np.ndarray) -> bool:

    if get_row(bygram[0], matrix) == get_row(bygram[1], matrix):
        return True

    return False


def check_cols(bygram: str, matrix: np.ndarray) -> bool:

    if get_col(bygram[0], matrix) == get_col(bygram[1], matrix):
        return True

    return False


def pleif_row(bygram: str, matrix: np.ndarray, mode: int) -> List[str]:
    num_cols = matrix.shape[1]
    shift = 1 if mode == MODE.ENCRYPT else -1
    return [
        matrix[get_row(item, matrix)][(get_col(item, matrix) + shift) % num_cols]
        for item in bygram
    ]


def pleif_col(bygram: str, matrix: np.ndarray, mode: int) -> List[str]:
    num_rows = matrix.shape[0]
    shift = 1 if mode == MODE.ENCRYPT else -1
    return [
        matrix[(get_row(item, matrix) + shift) % num_rows][get_col(item, matrix)]
        for item in bygram
    ]


def pleif_square(bygram: str, matrix: np.ndarray) -> List[str]:

    return [
        matrix[get_row(bygram[0], matrix), get_col(bygram[1], matrix)],
        matrix[get_row(bygram[1], matrix), get_col(bygram[0], matrix)],
    ]


def get_pleif(bygrams: List[str], key_matrix: np.ndarray, mode: int) -> List[str]:
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


def enc(text: str, alph: str = default_alph, key: str = "штурм") -> str:
    mode = MODE.ENCRYPT
    alph = remove_items_in_str(alph, "ё")
    text = clear_text(text.lower(), alph)

    bygrams = get_bygrams(text)
    key_matrix = get_key_matrix(key, alph)
    print(key_matrix)

    result = get_pleif(bygrams, key_matrix, mode)

    return "".join(result)


def dec(text: str, alph: str = default_alph, key: str = "штурм") -> str:
    mode = MODE.DECRYPT
    alph = remove_items_in_str(alph, "ё")
    text = clear_text(text.lower(), alph)

    bygrams = get_bygrams(text)
    key_matrix = get_key_matrix(key, alph)
    print(key_matrix)

    result = get_pleif(bygrams, key_matrix, mode)

    return "".join(result)


def main():
    from ..tests.test import test_crypt

    test_crypt(enc, dec)


if __name__ == "__main__":
    main()
