def extended_euclidean_algorithm(a: int, b: int) -> (int, int, int):
    """
    Возвращает кортеж из трёх элементов (gcd, x, y), такой, что
    a * x + b * y == gcd, где gcd - наибольший
    общий делитель a и b.

    В этой функции реализуется расширенный алгоритм
    Евклида и в худшем случае она выполняется O(log b).
    """
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t


def inverse_of(n: int, p: int) -> int:
    """
    Возвращает обратную величину
    n по модулю p.

    Эта функция возвращает такое целое число m, при котором
    (n * m) % p == 1.
    """
    gcd, x, y = extended_euclidean_algorithm(n, p)
    assert (n * x + p * y) % p == gcd

    if gcd != 1:
        # Или n равно 0, или p не является простым.
        raise ValueError(f"{n} no multiplicative inverse " "mod {p}")
    else:
        return x % p


def co_prime(a: int, b: int) -> bool:
    """
    Проверяет взаимно просты ли числа a и b
    """

    from math import gcd

    return gcd(a, b) == 1


def primes(n):
    """
    Факторизация числа n
    """
    primfac = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    return primfac


def random_of_ranges(*ranges):
    from random import choice

    all_ranges = sum(ranges, [])
    return choice(all_ranges)
