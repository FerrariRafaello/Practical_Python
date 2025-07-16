# Defining a simple Person class
class Person(object):

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def get_person(self):
        return "Person: {}, {}".format(self.name, self.age)

# Creating a Person instance
p = Person("Marco", 28)

print("Object type:", type(p), "Memory address:", id(p))
print(p.get_person())  # Shows the person's info

# -------------------------------------

# Simple class to sum numbers
class Adder:

    def __init__(self) -> None:
        self.total = 0

    def add(self, value):
        self.total += value

ad = Adder()
for i in range(10):
    ad.add(i)  # Adds 0 + 1 + ... + 9 = 45
print("Sum from 0 to 9:", ad.total)

# -------------------------------------

# Example of class method usage and composition
class A(object):
    def a1(self):
        print("Method a1 from class A")

class B(object):
    def b(self):
        print("Method b from class B")
        # Create a new A object and call its a1 method
        A().a1()

objB = B()
objB.b()
