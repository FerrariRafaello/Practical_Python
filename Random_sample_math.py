# 1. Counting numbers divisible by 3 and 4 in a range
counter = 0
for x in range(1000, 9001):
    if (x % 4 == 0) and (x % 3 == 0):
        print(f'{x} is divisible by 4 and by 3')
        counter += 1  # Only count if it matches both conditions
print(f'There are {counter} numbers divisible by both 3 and 4 in the range.\n')

# 2. Negative even numbers divisible by 3 or 4
for x in range(0, -30, -2):
    if x % 3 == 0:
        print(abs(x), 'even number divisible by 3')
    elif x % 4 == 0:
        print(abs(x), 'even number divisible by 4')
print()  # Just for separation

# 3. Power with math.pow
import math
x = math.pow(2, 1.25)
print("2 raised to 1.25 is:", x, "\n")

# 4. Random selection from string, list, tuple
import random
string = 'abacate laranja tomate'.split()  # convert to list for random.choice
print("Random word from string:", random.choice(string))

lista = ['abacate', 'laranja', 'tomate']
print("Random word from list:", random.choice(lista))

tupla = ('abacate', 'laranja', 'tomate')
print("Random word from tuple:", random.choice(tupla), "\n")

# 5. Random integer and random range
print("Random integer between 1 and 6:", random.randint(1, 6))
print("Random number (start 1, stop before 6, step 3):", random.randrange(1, 6, 3), "\n")

# 6. Randomly shuffle a list multiple times
names = ['alice', 'bob', 'carl', 'daniele', 'edgard']
for n in range(5):
    random.shuffle(names)
    print(f'On shuffle number {n + 1} the list was: {names}')
print()

# 7. Randomly pairing names and grades, shuffling both lists
names = ['alice', 'bob', 'carl', 'daniele', 'edgard']
grades = [7.1, 8.9, 5.2, 6.6, 9.9]

for x in range(5):
    shuffled_names = random.sample(names, k=len(names))
    shuffled_grades = random.sample(grades, k=len(grades))
    for y in range(5):
        print(f'On shuffle number {x + 1}, pair: {shuffled_names[y]} {shuffled_grades[y]}')
print()
