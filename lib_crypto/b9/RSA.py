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

from ..utils.def_str import clear_text
from ..utils.hash import hash
from ..utils.math import co_prime, inverse_of
from ..utils.print import print_kv

p, q, e, d = 3557, 2579, 3, 25  # example


def generate_ecp(msg, p=p, q=q, e=e):

    assert all(isprime(i) for i in (p, q)), "Числа P и Q должны быть простыми"

    n = p * q
    assert 1 < len(msg) < n, "Длина сообщения должна ∈ (1,n)"

    h = hash(msg)
    print_kv("Hash", h)

    euler = (p - 1) * (q - 1)  # Функция Эйлера
    assert co_prime(e, euler), "Числа E и φ(N) должны быть взаимно простыми"

    d = inverse_of(e, euler)

    return (h ** d) % n


def check(msg, ecp, e=e, n=p * q):
    h_1 = hash(msg)
    h = (ecp ** e) % n

    return h == h_1


def main():
    from ..utils.data import text_1000, text_test

    p, q, e, d = 7, 17, 7, 25
    h = 10

    msg = clear_text(text_test)
    ecp = generate_ecp(msg)
    chk = check(msg, ecp)

    print_kv("Подпись для пословицы", ecp)
    print_kv("Проверяем подпись", chk)

    msg = clear_text(text_1000)

    ecp = generate_ecp(msg)
    chk = check(msg, ecp)

    print_kv("Подпись для 1000", ecp)
    print_kv("Проверяем подпись", chk)


if __name__ == "__main__":
    main()
