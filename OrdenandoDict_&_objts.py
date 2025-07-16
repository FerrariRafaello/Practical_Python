# List of dictionaries (records)
rows = [
    {"name": "marcos", "age": 28},
    {"name": "joao", "age": 19},
    {"name": "maria", "age": 20},
    {"name": "pedro", "age": 30},
]

# Sorting by a common key
from operator import itemgetter

rows_by_name = sorted(rows, key=itemgetter("name"))
rows_by_age = sorted(rows, key=itemgetter("age"))
print(rows_by_name)
print(rows_by_age)

# Sorting by multiple keys with itemgetter:
order = sorted(rows, key=itemgetter("name", "age"))
print(order)

"""
itemgetter can also be used with min and max
Example:
lst = [{'age':28}, {'age':15}, {'age':20}]
print(min(lst, key=itemgetter('age')))  # Smallest by 'age'
print(max(lst, key=itemgetter('age')))  # Largest by 'age'
"""

# Sorting objects

class Object:
    def __init__(self, obj, name=None):
        self.obj = obj
        self.name = name

    def __repr__(self):
        return f"{self.obj}:{self.name}"

# List of objects
objects = [Object("90"), Object("30"), Object("20")]
print(objects)

# Using lambda to sort by .obj attribute
c = sorted(objects, key=lambda obj: obj.obj)
print(c)

from operator import attrgetter

# Using attrgetter to sort by .obj attribute
c1 = sorted(objects, key=attrgetter("obj"))
print(c1)

# More complex example with two attributes
guitar_samples = [Object(90, "claudio"), Object(30, "joao"), Object(55, "caio")]
c2 = sorted(guitar_samples, key=attrgetter("name", "obj"))
print(guitar_samples)
print(c2)

# Sorting by .obj attribute using lambda
c3 = sorted(guitar_samples, key=lambda obj: obj.obj)
print(c3)
