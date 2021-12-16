from dataclasses import dataclass

from ..utils.math import inverse_of


@dataclass
class Point:
    x: int
    y: int

    def __str__(self):
        return f"P({self.x}, {self.y})"


class ElepticCurve:
    def __init__(self, p, a, b):
        self.p = p

        assert pow(2, p - 1, p) == 1

        self.a = a
        self.b = b

        assert (4 * a ** 3 + 27 * b ** 2) % p != 0

    def __str__(self):
        a = abs(self.a)
        b = abs(self.b)

        a_sign = "-" if self.a < 0 else "+"
        b_sign = "-" if self.b < 0 else "+"

        return "y^2 = (x^3 {} {}x {} {}) mod {}".format(a_sign, a, b_sign, b, self.p)

    def mult(self, point, n):

        if n < 0:
            return self.neg(self.mult(-n, point))

        result = None
        addend = point

        while n:
            if n & 1:
                result = self.add(result, addend)
            addend = self.double(addend)
            n >>= 1

        return result

    def neg(self, point):

        if point is None:
            return None

        x, y = point
        result = Point(x, -y % self.p)

        return result

    def double(self, point):
        return self.add(point, point)

    def add(self, point1, point2):

        if point1 is None:
            return point2
        if point2 is None:
            return point1

        x1, y1 = point1.x, point1.y
        x2, y2 = point2.x, point2.y

        if x1 == x2 and y1 != y2:
            # point1 + (-point1) = 0
            return None

        if x1 == x2:
            lambda_ = (3 * x1 * x1 + self.a) * inverse_of(2 * y1, self.p)
        else:
            lambda_ = (y1 - y2) * inverse_of(x1 - x2, self.p)

        x3 = lambda_ ** 2 - x1 - x2
        y3 = lambda_ * (x3 - x1) + y1

        R = Point(x3 % self.p, -y3 % self.p)

        return R
