# Example: Returning functions from a function (function factory)

def parent(num):
    # Nested function definitions
    def child1():
        print("Child one")

    def child2():
        print("Child two")

    # Assert is used for checking preconditions; will raise AssertionError if false
    try:
        assert num == 20
        return child1  # If assertion passes, return child1
    except AssertionError:
        return child2  # If assertion fails, return child2

# f1 and f2 become function objects, not the result of the functions
f1 = parent(10)   # num != 20, so returns child2
f2 = parent(20)   # num == 20, so returns child1

f1()  # Output: Child two
f2()  # Output: Child one

