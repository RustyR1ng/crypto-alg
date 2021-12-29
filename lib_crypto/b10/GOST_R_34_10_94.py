"""
р - большое простое число длиной от 509 до 512 бит либо от 1020 до 1024 бит;
q - простой сомножитель числа (р -1), имеющий длину 254...256 бит;
а - любое число, большее 1 и меньшее (р-1), причем такое, что аq mod p=1;
х - некоторое число, меньшее q;
у = (а^x) mod р
"""

"""
Первые три параметра р, q и а являются открытыми и могут быть общими
для всех пользователей сети. Число х является секретным ключом. Число y является
открытым ключом. Чтобы подписать некоторое сообщение m, а затем проверить
подпись, выполняются следующие шаги.

1. Пользователь А генерирует случайное число k, причем k<q.
2. Пользователь А вычисляет значения
r = (а^k mod p) mod q,
s = (х * r + k * (Н(m))) mod q.
Если Н(m) mod q=0, то значение Н(m) mod q принимают равным единице.
Если r=0, то выбирают другое значение k и начинают снова.
Цифровая подпись представляет собой два числа:
r mod 2^256 и s mod 2^256
3. Пользователь А отправляет эти числа пользователю В.
4. Пользователь В проверяет полученную подпись, вычисляя
v = (Н(m)^(q-2)) mod q,
z1 = (s * v) mod q,
z2 = ((q-r) * v) mod q,
u = ((а^z1 * у^z2 ) mod р) mod q.
5. Если u = r, то подпись считается верной.
"""

from typing import Union

from ..utils.def_str import clear_text as ct
from ..utils.hash import kv_hash
from ..utils.math import primes


def get_hash(
    message: str,
    q: int,
    h: int = None,
):
    hashed_m = h if h else kv_hash(message)
    hashed_m = 1 if hashed_m % q == 0 else hashed_m

    return hashed_m


def enc(text: str, P: str, Q: str, A: str, X: str, K: str, h: int = None):
    P, Q, A, X, K = map(int, (P, Q, A, X, K))
    assert Q in primes(P - 1), "Q должно быть множителем для P-1"
    assert (A ** Q) % P == 1, "Условие (a**q)%p==1 не соблюдено"
    assert 1 < A < (P - 1), "A должно ∈ (1, P-1)"
    assert X < Q, "X должно быть < Q"
    assert K < Q, "K должно быть < Q"

    text = ct(text)

    text_hash = get_hash(text, Q, h)

    r = ((A ** K) % P) % Q
    assert r != 0, "R не должен = 0. Попробуйте ввести другие параметры"

    s = (X * r + K * text_hash) % Q
    return f"{r},{s}"


# y = (pub_key.a ** x) % pub_key.p
def dec(text: str, P: str, Q: str, A: str, Y: str, ecp: str, h: int = None):
    r, s = map(int, ecp.split(","))
    P, Q, Y, A = map(int, (P, Q, Y, A))
    text = ct(text)

    hashed_m = get_hash(text, Q, h)

    v = (hashed_m ** (Q - 2)) % Q
    z1 = (s * v) % Q
    z2 = ((Q - r) * v) % Q
    u = ((A ** z1 * Y ** z2) % P) % Q

    return u == r


def main():
    from ..data import text_1000, text_test
    from ..utils.printing import print_kv

    p, q, a = 23, 11, 6
    k = 5
    x = 8
    y = (a ** x) % p

    ecp = enc(text_test, p, q, a, x, k)
    chk = dec(text_test, p, q, a, y, ecp)
    print_kv("Подпись пословицы", ecp)
    print_kv("Проверка подписи", chk)

    ecp = enc(text_1000, p, q, a, x, k)
    chk = dec(text_1000, p, q, a, y, ecp)

    print_kv("Подпись 1000", ecp)
    print_kv("Проверка подписи", chk)


if __name__ == "__main__":
    main()
