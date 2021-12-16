from typing import Union

from sympy import isprime

from ..utils.def_str import clear_text as ct
from ..utils.hash import hash
from ..utils.math import co_prime
from ..utils.math import extended_euclidean_algorithm as EEA
from ..utils.math import inverse_of


class Elgaml_ECP:
    def __init__(self, P: int, G: int):
        assert isprime(P)
        assert G < P
        self.P = P
        self.G = G

    def get_public_key(self, X: int):
        P, G = self.P, self.G
        assert 1 < X <= (P - 1)
        Y = (G ** X) % P
        return Y

    def gen_ecp(self, msg: str, K: int, X: int, h=None):
        P, G = self.P, self.G
        assert 1 < K < (P - 1) and co_prime(K, (P - 1))

        msg = ct(msg)

        h = hash(msg) if h is None else h
        assert 1 < h < (P - 1)

        a = (G ** K) % P
        b = ((h - X * a) * inverse_of(K, P - 1)) % (P - 1)
        return (a, b)

    def check_ecp(self, msg: str, ecp: Union[int, int], public_key: int, h=None):
        P, G = self.P, self.G
        a, b = ecp
        msg = ct(msg)
        h = hash(msg) if h is None else h

        A1 = ((public_key ** a) * (a ** b)) % P
        A2 = (G ** h) % P

        return A1 == A2


def main():
    from ..utils.data import text_1000, text_test
    from ..utils.print import print_kv

    P, G = 11, 7

    crypter = Elgaml_ECP(P, G)

    X = 3
    K = 9

    msg = ""
    h = 5

    ecp = crypter.gen_ecp(msg, K, X, h)

    chk = crypter.check_ecp(msg, ecp, crypter.get_public_key(X), h)

    print_kv("Подпись примера", ecp)

    print_kv("Проверка подписи", chk)

    ecp = crypter.gen_ecp(text_test, K, X)
    chk = crypter.check_ecp(text_test, ecp, crypter.get_public_key(X))

    print_kv("Подпись пословицы", ecp)
    print_kv("Проверка подписи", chk)

    ecp = crypter.gen_ecp(text_1000, K, X)
    chk = crypter.check_ecp(text_1000, ecp, crypter.get_public_key(X))

    print_kv("Подпись 1000", ecp)
    print_kv("Проверка 1000", chk)


if __name__ == "__main__":
    main()
