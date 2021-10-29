def evklid_gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2


def ex_gcd(a, m):
    d = evklid_gcd(a, m)
    a0, a1 = a, m
    x0, x1 = 1, 0
    y0, y1 = 0, 1

    while a1 != 0:
        q = a0 // a1
        a0, a1 = a1, a0 - a1 * q
        x0, x1 = x1, x0 - x1 * q
        y0, y1 = y1, y0 - y1 * q

    return a0, x0
