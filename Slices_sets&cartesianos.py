# Naming slices for better use with objects/lists
lst = [1, 2, 3, 4, 5, 6, 7]
first_three = slice(0, 3)
print(first_three)
print(lst[first_three])
last_three = slice(-3, None)
print(lst[last_three])

# ----------------------------------
# SETS
c = {1, 2, 3, 4, 5}
d = {3, 3, 4, 4, 6, 7}
print(c)
print(d)  # Duplicate numbers are "banned" in a set

# Union of both sets:
e = c | d
print(e)

# Numbers present in both sets:
f = c & d
print(f)

# Elements in c but not in d:
g = c - d
print(g)

# Elements in either c or d, but not both:
h = c ^ d
print(h)

# ----------------------------------
# Cartesian products with itertools

import itertools

for p in itertools.product([1, 2, 3], [4, 5]):
    print(p)
"""
Visualize as a matrix multiplication:
each element from the first iterable is paired with each element from the second.
"""