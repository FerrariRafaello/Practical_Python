import numpy as np

# Regular Python list
l = [1, 2, 3]
print(l)

# List multiplied by 8: repeats the elements 8 times
print(l * 8)  # [1, 2, 3, 1, 2, 3, ..., 1, 2, 3] (8 times)
# print(l**4)  # TypeError: unsupported operand

# Now, let's use NumPy arrays:
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(x * 8)      # Each element multiplied by 8: [8, 16, 24]
print(x**4)       # Each element to the power of 4: [1, 16, 81]
print(x + 9)      # Add 9 to each element: [10, 11, 12]

# Calculate "y1": elementwise multiplication with different numbers
y1 = (y[0] * 4, y[1] * 5, y[2] * 6)
print(y1)

# Square root of each value in y1 (needs to be np.array for np.sqrt)
raiz = np.sqrt(np.array(y1))
print(raiz)

# Changing values in the array
print(x)
x[0] = x[0] * 3
print(x)

# Creating a matrix
mat = np.matrix([[1, 2], [3, 4]])  # 2x2 matrix
print(mat)

# Transpose: swap rows and columns
transpose = mat.T
print(transpose)

# Inverse of the matrix
inverse = mat.I
print(inverse)

# -----------------------------------
# Random module for randomness

import random

lst = [1, 2, 3, 4, 5, 6]

print(random.choice(lst))  # Randomly select one element

# Sample a subset of items
print(random.sample(lst, 3))  # Sample of 3
print(random.sample(lst, 5))  # Sample of 5

# Shuffle the items in the list (in place)
random.shuffle(lst)
print(lst)

# Generate random integers (inclusive)
print(random.randint(0, 10))  # Between 0 and 10

# Generate random float between 0 and 1
print(random.random())

# -----------------------------------
# Docstrings

"""
Docstrings are used to explain the code for others.
They can include text, links, explanations, etc., and should be placed right after function or class definitions.
"""

def multiply(x, y):
    """Returns the multiplication of two numbers."""
    return x * y

# Docstrings can be viewed with help():
help(multiply)
# Or directly:
print(multiply.__doc__)

class MyClass:
    """A class that does nothing."""
    pass

print(MyClass.__doc__)

# Comments are nice...
"""And more docstrings, too."""
