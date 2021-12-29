from dataclasses import dataclass
from random import randint
from typing import List

from ..utils.def_str import clear_text, to_indexes, to_symbols
from ..utils.math import inverse_of


@dataclass
class OpenKey:
    p: int
    g: int
    y: int


@dataclass
class PrivKey:
    x: int


def gen_x(p):

    return randint(2, p - 1)


def check_x(x, p):
    assert 2 < x < p - 1, "X должно принадлежать (2, p-1)"


def gen_y(g, x, p):

    return (g ** x) % p


def gen_keys(p, g, x=None):

    x = gen_x(p) if not x else x
    y = gen_y(g, x, p)

    return OpenKey(p, g, y), PrivKey(x)


class Elgamal:
    def __init__(self):
        pass

    def __str__(self):
        return "\n".join(
            [
                "Elgamal Crypter",
                f"Открытый ключ : {self.open_key}",
                f"Закрытый ключ : {self.priv_key}",
            ]
        )

    def enc(self, msg: str, k=None) -> str:

        p, g, y = self.open_key.p, self.open_key.g, self.open_key.y

        msg = to_indexes(clear_text(msg))
        enc_m = []

        for num in msg:
            k = randint(2, p - 2)
            a = (g ** k) % p
            b = ((y ** k) * num) % p

            enc_m.append(a)
            enc_m.append(b)
        enc_m = " ".join(list(map(str, enc_m)))
        return enc_m

    def dec(self, e_msg: str, p=None) -> str:
        e_msg = list(map(int, e_msg.split(" ")))
        p = p if p else self.open_key.p
        x = self.priv_key.x
        d_msg = []

        for i in range(0, len(e_msg), 2):

            a, b = e_msg[i], e_msg[i + 1]
            d_msg.append(((inverse_of(a ** x, p) * b)) % p)
        print(d_msg)
        return to_symbols(d_msg)


def enc(text: str, p: str, g: str, y: str) -> str:
    p, g, y = int(p), int(g), int(y)
    open_key = OpenKey(p, g, y)

    crypter = Elgamal()
    crypter.open_key = open_key

    return crypter.enc(text)


def dec(text: str, p: str, x: str) -> str:
    p, x = int(p), int(x)
    priv_key = PrivKey(x)

    crypter = Elgamal()
    crypter.priv_key = priv_key

    return crypter.dec(text, p)


def main():
    from ..tests.test import test_crypt

    crypter = Elgamal()
    crypter.open_key = OpenKey(37, 2, 35)
    crypter.priv_key = PrivKey(19)
    test_crypt(crypter.enc, crypter.dec)


if __name__ == "__main__":
    main()
