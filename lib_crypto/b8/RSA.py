from typing import List

from ..utils.math import inverse_of
from ..utils.def_str import clear_text, to_indexes, to_symbols


class RSA:
    def __init__(self, open_key: List[int], private_key: List[int]):
        assert open_key[1] == private_key[1]
        self.open_key = open_key
        self.private_key = private_key

    @classmethod
    def init_params(cls, p: int, q: int, e: int):
        n = p * q
        euler = (p - 1) * (q - 1)  # Функция Эйлера

        d = inverse_of(e, euler)  # Cекретная экспонента

        return cls((e, n), (d, n))

    def __str__(self):
        items = [f"n = {self.n}", f"e = {self.e}", f"d = {self.d}"]
        keys = [
            f"Открытый ключ: {self.open_key}",
            f"Секретный ключ: {self.private_key}",
        ]
        res = ["\n".join(s) for s in [items, keys]]
        return "\n" + "\n".join(res) + "\n"

    @property  # Открытый ключ
    def open_key(self):
        return self.e, self.n

    @open_key.setter
    def open_key(self, key):
        self.n = key[1]
        self.e = key[0]

    @property  # Закрытый ключ
    def private_key(self):
        return self.d, self.n

    @private_key.setter
    def private_key(self, key):
        self.n = key[1]
        self.d = key[0]

    def enc_1(self, num: int):
        return (num ** self.e) % self.n

    # Шифрование
    def enc(self, m: str):
        m = to_indexes(clear_text(m))
        enc_m = [self.enc_1(symbol) for symbol in m]
        return enc_m

    def dec_1(self, num: int):
        return (num ** self.d) % self.n

    # Расширвание
    def dec(self, enc_m: List[int]):
        m = [self.dec_1(symbol) for symbol in enc_m]
        m = to_symbols(m)
        return m


def main():
    from ..utils.test import test_crypt

    encrypter = RSA((23, 247), (47, 247))
    test_crypt(encrypter.enc, encrypter.dec)


if __name__ == "__main__":
    main()
