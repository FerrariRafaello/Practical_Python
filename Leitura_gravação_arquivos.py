# Reading data from text files

print('Opening a file for reading:')
with open('contacts.txt', 'r') as file:
    content = file.read()
    print(content)
print('File closed.')

print('\nCreating a new file:')
with open('contacts1.txt', 'w') as file:
    line = 'Harriet, 3555-0001\n'
    file.write(line)
print('Opening the file again to check the information:')
with open('contacts1.txt', 'r') as file:
    content = file.read()
    print(f'The content of contacts1.txt is:\n{content}')
print('File closed.')

print('Replacing the content of contacts1.txt:')
with open('contacts1.txt', 'w') as file:
    line = 'Harriet, 3555-1000\n'
    file.write(line)
print('Opening contacts1.txt again to check the information:')
with open('contacts1.txt', 'r') as file:
    content = file.read()
    print(f'The content of contacts1.txt is:\n{content}')
print('Harriet\'s phone number changed from 3555-0001 to 3555-1000')
print('File closed.')

print('\nAdding a new contact to contacts1.txt:')
with open('contacts1.txt', 'a') as file:
    line = 'Ivan, 3555-1221\n'
    file.write(line)
print('Opening contacts1.txt again to check the information:')
with open('contacts1.txt', 'r') as file:
    content = file.read()
    print(f'The content of contacts1.txt is:\n{content}')

print('Updating the content of contacts1.txt:')
with open('contacts1.txt', 'r+') as file:
    line = 'Harriet, 3555-1001\n'
    file.write(line)
    line = 'Ivan, 3555-1223\n'
    file.write(line)
    file.seek(0)
    content = file.read()
    print(f'The content of contacts1.txt is:\n{content}')

print('Adding information to contacts1.txt at the end of the file:')
with open('contacts1.txt', 'a+') as file:
    line = 'Janet, 3555-1002\n'
    file.write(line)
    line = 'Karla, 3555-1003\n'
    file.write(line)
    file.seek(0)
    content = file.read()
    print(f'The content of contacts1.txt is:\n{content}')

print('Changing all content of contacts1.txt:')
with open('contacts1.txt', 'w+') as file:
    line = 'Lucy, 3555-1004\n'
    file.write(line)
    line = 'Mary, 3555-1005\n'
    file.write(line)
    file.seek(0)
    content = file.read()
    print(f'The content of contacts1.txt is:\n{content}')
