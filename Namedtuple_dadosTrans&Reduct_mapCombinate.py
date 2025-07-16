from collections import namedtuple, ChainMap

# Namedtuple (immutable tuple with named fields)
Subscriber = namedtuple("Subscriber", ["id", "email"])  # immutable
sub = Subscriber(id="1000", email="mcastrosouza@live.com")
print(sub)

# Accessing fields individually
one = sub.id
two = sub.email
print(one, "\n", two)

# Unpacking:
length = len(sub)
print(length)

id, email = sub
print(id)
print(email)

# Using _replace to create a modified copy (since namedtuple is immutable)
sub = sub._replace(id=101)
print(sub.id)

# Reduction functions: sum, max, min, etc.
numbers = [10, 5, 20, 8]
total = sum(numbers)
print(total)

maxi = max(numbers)
print(maxi)

mini = min(numbers)
print(mini)

# Getting the sum of squares of the elements in a list
numbers1 = [1, 2, 3]
sum_squares = sum([x * x for x in numbers1])
print(sum_squares)

# Same, but using a generator expression (more memory efficient)
sum_squares_gen = sum(x * x for x in numbers1)
print(sum_squares_gen)

# Lambda test (not used)
test = lambda x: x ** x
print(test(3))  # Just to show it works

# Combining multiple mappings (dicts) into a single view
a = {"x": 1, "z": 3}
b = {"y": 2, "z": 4}
# Combine using ChainMap
c = ChainMap(a, b)
print(c)

"""
If there are duplicate keys, the key from the first mapping takes precedence.
"""
print(c["x"])  # from a
print(c["y"])  # from b
print(c["z"])  # from a (3, not 4)

# Operations:
count = len(c)  # counts unique keys: x, y, z == 3
print(count)

# Deleting a key (only deletes from the first dict)
del c["x"]
print(c)

# Adding back
a["x"] = 1
print(a)

# Merging into a new dict (useful for making a real combined copy)
merged = dict(b)
merged.update(a)
print(merged["x"])  # from a
print(merged["y"])  # from b
print(merged["z"])  # from a, as update gives precedence to the last updated

"""
If any of the original dictionaries are changed,
the changes are NOT reflected in the merged dictionary.
"""

# However, changes to original dicts are reflected in the ChainMap:
a["z"] = 7
print(c["z"])  # Now shows 7
