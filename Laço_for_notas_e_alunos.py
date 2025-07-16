students = ['alice', 'bob', 'carl', 'danielle']
# List of student names

grades = [9.5, 8.0, 9.5, 8.0]
# List of grades for each student (in the same order)

# enumerate pairs each student with their index, making it easy to match names to grades
for index, student in enumerate(students):
    print(f'Name: {student} - Grade: {grades[index]}')
    # {student} = alice, bob, etc.; grades[index] = grade for each student
