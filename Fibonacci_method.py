# Fibonacci sequence: each number is the sum of the previous two numbers

n = int(input('How many Fibonacci numbers do you want to see? '))

# Start with the first two numbers in the sequence
a, b = 1, 1

print("Fibonacci sequence:")

if n >= 1:
    print(a, end=' ')
if n >= 2:
    print(b, end=' ')

for _ in range(3, n + 1):
    next_fib = a + b     # Calculate the next number in the sequence
    print(next_fib, end=' ')
    a, b = b, next_fib   # Update the two previous numbers

print()  # Just a newline at the end
