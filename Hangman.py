# Simple hangman-style guessing game

word = 'madagascar'
guessed_letters = []  # List to store guessed letters
chances = 3

while True:
    if chances < 1:
        print('You lost!')
        break

    letter = input('Enter a letter: ').lower()

    if len(letter) != 1:
        print('Invalid input! Please enter only one letter.')
        continue

    if letter in guessed_letters:
        print('You have already guessed that letter.')
        continue

    guessed_letters.append(letter)

    if letter in word:
        print('Correct letter:', letter)
    else:
        print('The letter', letter, 'is not in the word.')
        chances -= 1
        print('You have', chances, 'chances left.')

    # Build the display of the current guessed state
    temp_word = ''
    for secret_letter in word:
        if secret_letter in guessed_letters:
            temp_word += secret_letter
        else:
            temp_word += '*'

    print('Current progress:', temp_word)

    if temp_word == word:
        print('Congratulations, you won!')
        break
