def __radd__(self, other):
    if isinstance(other, int):
        other = Fraction(other, 1)
    return self.__add__(other)