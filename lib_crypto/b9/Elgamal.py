from typing import Union

from sympy import isprime

from ..utils.def_str import clear_text as ct
from ..utils.hash import kv_hash
from ..utils.math import co_prime, inverse_of


def check_pub_params(P: int, G: int):
    assert isprime(P), "P должно быть простым"
    assert G < P, "Условие G < P не соблюдено"


def enc(text: str, K: str, X: str, P: str, G: str, text_hash=None):
    K, X, P, G = map(int, (K, X, P, G))
    check_pub_params(P, G)
    assert 1 < X <= (P - 1), "X должно ∈ (1, P-1)"
    assert 1 < K < (P - 1), "K должно ∈ (1, P-1)"
    assert co_prime(K, (P - 1)), "K и P-1 должеы быть взаимно простыми"

    text = ct(text)
    text_hash = kv_hash(text) if text_hash is None else text_hash
    assert (
        1 < text_hash < (P - 1)
    ), "Хэш текста должен ∈ (1,P-1). Попробуйте выбрать другие параметры"

    a = (G ** K) % P
    b = ((text_hash - X * a) * inverse_of(K, P - 1)) % (P - 1)
    return f"{a},{b}"


# pub_key = (G ** X) % P
def dec(text: str, ecp: str, public_key: str, P: str, G: str, text_hash=None):
    a, b = map(int, ecp.split(","))
    P, G, public_key = map(int, (P, G, public_key))
    check_pub_params(P, G)

    text = ct(text)
    h = kv_hash(text) if text_hash is None else text_hash

    A1 = ((public_key ** a) * (a ** b)) % P
    A2 = (G ** h) % P

    return A1 == A2


def main():
    from ..data import text_1000, text_test
    from ..utils.printing import print_kv

    P, G = 11, 7
    X = 3
    K = 9
    h = 5

    ecp = enc("", K, X, P, G, h)
    chk = dec("", ecp, 2, P, G, h)

    print_kv("Подпись примера", ecp)
    print_kv("Проверка подписи", chk)

    ecp = enc(text_test, K, X, P, G)
    chk = dec(text_test, ecp, 2, P, G)

    print_kv("Подпись пословицы", ecp)
    print_kv("Проверка подписи", chk)

    ecp = enc(text_1000, K, X, P, G)
    chk = dec(text_1000, ecp, 2, P, G)

    print_kv("Подпись 1000", ecp)
    print_kv("Проверка 1000", chk)


if __name__ == "__main__":
    main()
