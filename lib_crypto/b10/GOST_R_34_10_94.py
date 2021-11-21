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

from dataclasses import dataclass
from itertools import chain
from ..utils.def_bin import count_bits_in_num as cbin
from ..utils.math import primes, random_of_ranges
from ..utils.def_str import clear_text as ct

# from random import getrandbits as randbits, randint, choice
from ..utils.hash import hash

import pygost

# RANGE_P = list(chain(range(509, 512), range(1020, 1024)))
# RANGE_Q = list(range(254, 256))


@dataclass
class PubKey:
    p: int  # = randbits(choice(RANGE_P))
    q: int  # = randbits(choice(RANGE_Q))
    a: int

    def __post_init__(self):
        p, a, q = self.p, self.a, self.q

        # assert cbin(p) in RANGE_P
        assert q in primes(p - 1)  # and cbin(p) in RANGE_Q
        assert (a ** q) % p == 1 and 1 < a < (p - 1)


class GOST94_ECP:
    def __init__(self, pub_key: PubKey, x: int = None, y: int = None):
        self.pub_key = pub_key
        if x:
            assert x < q
            self.x = x
            self.y = (pub_key.a ** x) % p
        elif y:
            self.y = y

    def get_hash(self, message: str, h: int = None):
        hashed_m = h if h else hash(message)
        hashed_m = 1 if hashed_m % self.pub_key.q == 0 else hashed_m

        return hashed_m

    def generate_ecp(self, message: str, k: int, h: int = None) -> (int, int):
        message = ct(message)
        p, q, a, x = self.pub_key.p, self.pub_key.q, self.pub_key.a, self.x
        assert k < q

        r = ((a ** k) % p) % q
        assert r != 0

        hashed_m = self.get_hash(message, h)
        s = (x * r + k * hashed_m) % q

        return r, s

    def check_ecp(self, message: str, r: int, s: int, h: int = None):
        message = ct(message)
        p, q, a, y = self.pub_key.p, self.pub_key.q, self.pub_key.a, self.y

        hashed_m = self.get_hash(message, h)

        v = (hashed_m ** (q - 2)) % q
        z1 = (s * v) % q
        z2 = ((q - r) * v) % q
        u = ((a ** z1 * y ** z2) % p) % q

        return u == r


if __name__ == "__main__":
    from ..utils.data import text_test, text_1000
    from ..utils.print import print_kv

    p, q, a = 23, 11, 6
    pk = PubKey(p, q, a)

    gost = GOST94_ECP(pk, 8)

    r, s = gost.generate_ecp(text_test, 5)
    chk = gost.check_ecp(text_test, r, s)

    print_kv("Подпись пословицы", (r, s))
    print_kv("Проверка подписи", chk)

    r, s = gost.generate_ecp(text_1000, 5)
    chk = gost.check_ecp(text_1000, r, s)

    print_kv("Подпись 1000", (r, s))
    print_kv("Проверка подписи", chk)
