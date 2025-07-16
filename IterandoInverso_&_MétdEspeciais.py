# How to iterate in reverse:

# Conventional way:
lst = [1, 2, 3]
for i in lst:
    print(i)

# To iterate in reverse, just use reversed():
for x in reversed(lst):
    print(x)

# -----------------------------------------------

# Special Methods
"""
Special methods (also called magic or dunder methods) are called by the Python interpreter,
not directly by the programmer.
"""

# Implementing the special method __add__ to sum complex numbers
class Complex:

    def __init__(self, real, imag) -> None:
        self.real = real
        self.imag = imag

    def __repr__(self):
        return f"({self.real}, {self.imag}i)"  # String representation

    def __add__(self, other):
        # Add real parts together and imaginary parts together
        return Complex(self.real + other.real, self.imag + other.imag)

# Creating two complex numbers
c1 = Complex(3, 1)
print(c1)
c2 = Complex(2, 4)
print(c2)

# Sum of real parts and imaginary parts
c3 = c1 + c2
print(c3)
