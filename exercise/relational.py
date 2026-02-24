# Equal to 
def __eq__(self, other):
    return self.num == other.num and self.den == other.den

# Not equal to 
def __ne__(self, other):
    return not self == other

# Less than
def __lt__(self, other):
    return self.num * other.den < self.den * other.num

# Less than or equal to 
def __le__(self, other):
    return self.num * other.den <= self.den * other.num

# Greater than
def __gt__(self, other):
    return self.num * other.den > self.den * other.num

# Greater than or equal to
def __ge__(self, other):
    return self.num * other.den >= self.den * other.num