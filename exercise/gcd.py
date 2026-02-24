def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

class Fraction:
    def __init__(self, num, den):
        common = gcd(num, den)
        self.num = num // common
        self.den = den // common