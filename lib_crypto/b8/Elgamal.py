from random import randint
from dataclasses import dataclass
from typing import List
from ..utils.math import pow_m1
from ..utils.def_str import clear_text, to_indexes, to_symbols


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


def gen_y(g, x, p):

    return (g ** x) % p


def gen_keys(p, g, x=None):

    x = gen_x(p) if not x else x
    y = gen_y(g, x, p)

    return OpenKey(p, g, y), PrivKey(x)


class Elgamal:
    def __init__(self, p: int, g: int, x: int = None):
        self.open_key, self.priv_key = gen_keys(p, g, x)

    def __str__(self):
        return "\n".join(
            [
                "Elgamal Crypter",
                f"Открытый ключ : {self.open_key}",
                f"Закрытый ключ : {self.priv_key}",
            ]
        )

    def enc(self, msg: str, k=None):

        p, g, y = self.open_key.p, self.open_key.g, self.open_key.y

        msg = to_indexes(clear_text(msg))
        enc_m = []

        for num in msg:
            k = randint(2, p - 2) if not k else k
            a = (g ** k) % p
            b = ((y ** k) * num) % p

            enc_m.append(a)
            enc_m.append(b)
        return enc_m

    def dec(self, e_msg: List[int]):
        x, p = self.priv_key.x, self.open_key.p
        d_msg = []

        for i in range(0, len(e_msg), 2):

            a, b = e_msg[i], e_msg[i + 1]
            d_msg.append(((pow_m1(a ** x, p) * b)) % p)

        return to_symbols(d_msg)


if __name__ == "__main__":
    from ..utils.test import test_crypt

    crypter = Elgamal(37, 2, 19)

    test_crypt(crypter.enc, crypter.dec)
