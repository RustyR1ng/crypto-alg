"""
1. Берутся два очень больших простых числа P и Q и находятся
произведение простых чисел N=P×Q и функция Эйлера от этого
произведения φ(N)=(P-1)×(Q-1).
2. Выбирается случайное целое число E, взаимно простое с φ(N), и
вычисляется
D=(1 MOD φ(N))/E.
3. Потом E и N публикуются как открытый ключ, D сохраняется в
тайне.
4. Если M — сообщение, а h(M) = m – хеш-код сообщения, длина
которого должна быть в интервале (1,N), то электронная цифровая
подписьS получается шифрованием хеш-кода сообщения m
возведением в степень D по модулю N: S = mD MOD N.
5. Получателю отправляется сообщение M и подпись S.
6. Получатель сообщения хеширует M, получает хеш-код m’.
7. Проверяет подпись S: расшифровывает хеш-код, возведя S в
степень E (число E ему известно) по модулю N: m = SE MOD N.
8. Сравнивает m и m’: если m = m’ - подпись верна.
"""
__all__ = ["generate_ecp", "check", "main"]

from sympy import isprime

from ..utils.def_str import clear_text as ct
from ..utils.hash import kv_hash
from ..utils.math import co_prime, inverse_of
from ..utils.printing import print_kv

p, q, e, d = 3557, 2579, 3, 25  # example


def enc(text: str, P: str, Q: str, E: str) -> int:
    P, Q, E = map(int, (P, Q, E))
    assert all(isprime(i) for i in (P, Q)), "Числа P и Q должны быть простыми"

    n = P * Q
    assert 1 < len(text) < n, "Длина сообщения должна ∈ (1,n)"

    text = ct(text)

    h = kv_hash(text)
    print_kv("Hash", h)

    euler = (P - 1) * (Q - 1)  # Функция Эйлера
    assert co_prime(E, euler), "Числа E и φ(N) должны быть взаимно простыми"

    d = inverse_of(E, euler)

    return (h ** d) % n


# n = p*q
def dec(text: str, ecp: str, E: str, N: str):
    ecp, E, N = map(int, (ecp, E, N))

    text = ct(text)

    h_1 = kv_hash(text)
    h = (ecp ** E) % N

    return h == h_1


def main():
    from ..data import text_1000, text_test

    P, Q, E = 7, 17, 7

    ecp = enc(text_test, P, Q, E)
    chk = dec(text_test, ecp, E, P * Q)

    print_kv("Подпись для пословицы", ecp)
    print_kv("Проверяем подпись", chk)

    ecp = enc(text_1000, P, Q, E)
    chk = dec(text_1000, ecp, E, P * Q)

    print_kv("Подпись для 1000", ecp)
    print_kv("Проверяем подпись", chk)


if __name__ == "__main__":
    main()
