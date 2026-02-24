# Str:used when you print:
print(f)

def __str__(self):
    return f"{self.num}/{self.den}"

# repr : used in interpreter 
def __repr__(self):
    return f"Fraction({self.num}, {self.den})"
