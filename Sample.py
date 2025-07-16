import random

names = ['alice', 'bob', 'carl', 'daniele', 'edgard']
grades = [7.1, 8.9, 5.2, 6.6, 9.9]

# Perform 5 random samplings of the full lists
for sample_number in range(5):
    shuffled_names = random.sample(names, k=len(names))
    shuffled_grades = random.sample(grades, k=len(grades))
    for i in range(len(names)):
        print(f'On shuffle number {sample_number + 1}, pairing: {shuffled_names[i]} {shuffled_grades[i]}')
