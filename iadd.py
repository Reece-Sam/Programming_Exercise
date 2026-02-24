# f1 += f2

def __iadd__(self, other):
    result = self + other
    self.num = result.num
    self.den = result.den
    return self