# Lists to store names and grades
names = ['', '', '', '', '']
grades = [0.0, 0.0, 0.0, 0.0, 0.0]

# Loop to collect input for 5 students
for i in range(5):
    print(f'Enter the name of student {i + 1}:')
    names[i] = input()
    print(f'Enter the grade for {names[i]}:')
    grades[i] = float(input())

# Calculate the average of the grades
average = sum(grades) / len(grades)
print('\nThe class average is: %.2f' % average)
