from dataclasses import dataclass

from ..utils.ElepticCurve import ElepticCurve, Point
from ..utils.math import inverse_of


class Elgamal:
    @dataclass
    class EncMessage:
        R: Point
        e: int

        def __repr__(self):
            return f"{(self.R, self.e)}"

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

    def encrypt(self, msg: int, k: int, public_key: Point):
        curve, q, G = self.curve, self.q, self.G

        assert msg < curve.p
        assert 0 < k < q

        R = curve.mult(G, k)
        P = curve.mult(public_key, k)

        e = (msg * P.x) % curve.p

        return Elgamal.EncMessage(R, e)

    def decrypt(self, e_msg: EncMessage, private_key: int):
        R, e = e_msg.R, e_msg.e
        Q = self.curve.mult(R, private_key)
        p = self.curve.p
        result = (e * inverse_of(Q.x, p)) % p

        return result


def main():
    from ..utils.print import print_kv

    p, a, b = 11, 2, -5
    curve = ElepticCurve(p, a, b)
    G = Point(5, 8)

    crypter = Elgamal(curve, G)

    msg, k = 10, 5
    priv_key = 4
    e_msg = crypter.encrypt(msg, k, crypter.get_public_key(priv_key))
    print_kv("Шифровка", e_msg)

    d_msg = crypter.decrypt(e_msg, priv_key)
    print_kv("Расшифровка", d_msg)


if __name__ == "__main__":
    main()
