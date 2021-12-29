from typing import List

from backend.lib_crypto.utils.math import inverse_of

from ..utils.def_str import clear_text, to_indexes, to_symbols


def enc_1(num: int, n: int, e: int):
    return (num ** e) % n


# Шифрование
def enc(text: str, p: str, q: str, e: str):
    p, q, e = map(int, (p, q, e))
    n = p * q
    euler = (p - 1) * (q - 1)  # Функция Эйлера
    d = inverse_of(e, euler)
    m = to_indexes(clear_text(text))
    enc_m = [enc_1(symbol, n, e) for symbol in m]

    return f"{enc_m} d={d}, n={n}"


def dec_1(num: int, d: int, n: int):
    return (num ** d) % n


# Расширвание
def dec(text: str, d: str, n: str):
    d, n = map(int, (d, n))
    m = [dec_1(symbol, d, n) for symbol in text]
    m = to_symbols(m)
    return m


def main():
    e, n = 23, 247
    d = 47


if __name__ == "__main__":
    main()
