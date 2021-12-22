from dataclasses import dataclass
from typing import Union

from ..utils.def_str import clear_text, to_indexes, to_symbols
from ..utils.ElepticCurve import ElepticCurve, Point
from ..utils.math import inverse_of


@dataclass
class EncMessage:
    R: Point
    e: int

    def __repr__(self):
        return f"{(self.R, self.e)}"


class Elgamal:
    def __init__(self, curve: ElepticCurve, G: Point):
        self.curve = curve
        self.G = G
        self.q = self.get_q()

    def get_public_key(self, private_key: int):
        assert 0 < private_key < self.q, f"Секретный ключ должен ∈ (0,{self.q})"
        return self.curve.mult(self.G, private_key)

    def get_q(self):
        res_point = Point(-1, -1)
        q = 2
        while res_point:
            res_point = self.curve.mult(self.G, q)
            q += 1
        return q

    def encrypt_symbol(self, sym: int, k: int, public_key: Point) -> Union[Point, int]:
        curve, q, G = self.curve, self.q, self.G

        assert sym < curve.p
        assert 0 < k < q

        R = curve.mult(G, k)
        P = curve.mult(public_key, k)

        e = (sym * P.x) % curve.p

        return R, e

    def decrypt_symbol(self, sym: int, private_key: int):
        R, e = sym.R, sym.e
        Q = self.curve.mult(R, private_key)
        p = self.curve.p
        result = (e * inverse_of(Q.x, p)) % p

        return result

    def encrypt(self, msg: str, k: int, public_key: Point):
        res = ""
        msg = clear_text(msg)
        msg = to_indexes(msg)
        for sym in msg:
            enc_symbol = self.encrypt_symbol(sym, k, public_key)
            enc_symbol = [enc_symbol[0].x, enc_symbol[0].y, enc_symbol[1]]
            enc_symbol = list(map(str, enc_symbol))
            res += "-".join(enc_symbol) + " "
        return res.strip()

    def decrypt(self, msg: str, private_key: int):
        res = []
        for sym in msg.split(" "):
            sym = sym.split("-")
            sym = list(map(int, sym))
            sym = EncMessage(Point(sym[0], sym[1]), sym[2])
            res.append(self.decrypt_symbol(sym, private_key))

        return to_symbols(res)


def main():
    from ..data import text_1000
    from ..utils.printing import print_kv

    p, a, b = 37, 17, -5
    curve = ElepticCurve(p, a, b)
    G = Point(5, 8)
    crypter = Elgamal(curve, G)

    k = 5
    priv_key = 4
    pub_key = crypter.get_public_key(priv_key)

    params = [k]
    e_msg = crypter.encrypt(text_1000, pub_key, *params)
    print_kv("Шифровка", e_msg)

    d_msg = crypter.decrypt(e_msg, priv_key)
    print_kv("Расшифровка", d_msg)


if __name__ == "__main__":
    main()
