# Substraction
from gcd import Fraction


def __sub__(self, other):
    new_num = self.num * other.den - self.den * other.num
    new_den = self.den * other.den
    return Fraction(new_num, new_den)

# Multiplication
def __mul__(self, other):
    return Fraction(self.num * other.num,
                    self.den * other.den)

# Truedev
def __truediv__(self, other):
    return Fraction(self.num * other.den,
                    self.den * other.num)