"""
В протоколе обмена секретными ключами предполагается, что все
пользователи знают некоторые числа n и a (1< a < n). Для выработки общего
секретного ключа пользователи A и B должны проделать следующую процедуру:
"""

"""
1. Определить секретные ключи пользователей КА и КВ.
2. Для этого каждый пользователь независимо выбирает случайные числа из
интервала (2,..., n-1).
3. Вычислить открытые ключи пользователей YA и YB:
 Y=a^K mod n
4. Обменяться ключами YA и YB по открытому каналу связи.
5. Независимо определить общий секретный ключ К:
 KA=Y^KA mod n
 KB=Y^KB mod n.

KA = KB = K
"""

from ..utils.printing import print_kv


def gen(n: int, a: int, priv_key_A: int, priv_key_B: int) -> int:
    assert 1 < a < n, "A должно принадлежать (1, n)"
    assert all(
        2 < i < (n - 1) for i in (priv_key_A, priv_key_B)
    ), "Секретные ключи должны принадлежать (2, n-1)"  # private keys

    pub_A, pub_B = (
        (a ** key) % n for key in (priv_key_A, priv_key_B)
    )  # public keys (yA, yB)

    key_A, key_B = (
        ((public ** private) % n)
        for public, private in zip((pub_A, pub_B), (priv_key_B, priv_key_A))
    )  # joint private key

    result_key = key_A if key_A == key_B and key_A > 1 else None

    return result_key


def main():
    n, a, key_A, key_B = 9, 4, 4, 5
    print_kv("n, a, key_A, key_B", (n, a, key_A, key_B))

    res = gen(n, a, key_A, key_B)
    print_kv("Ключ", res)


if __name__ == "__main__":
    main()
