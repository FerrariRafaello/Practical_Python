def show_calculator():
    print("""
              |-------------|
              |             |
              | Calculator  |
              | ___________ |
              | c        /  |
              | 7  8  9  *  |
              | 4  5  6  -  |
              | 1  2  3  +  |
              |    0        |
              |-------------|
    """)
    print('Press [c] to clear history.')
    print('Press [s] to exit.\n')


def print_history(history):
    if history:
        print('History:', ', '.join(f'{result:.2f}' for result in history))
    else:
        print('History is empty.')


def get_number(prompt):
    """Pede um número ao usuário ou permite sair digitando 's'."""
    while True:
        value = input(prompt).strip().lower()
        if value == 's':
            return None  # Retorna None para sinalizar que o usuário quer sair
        try:
            return float(value)
        except ValueError:
            print('Invalid number! Type a valid number or "s" to exit.')

def main():
    show_calculator()
    history = []
    current = None

    while True:
        # Get first number if needed
        if current is None:
            current = get_number('Enter the value: ')
            if current is None:
                print('\nThanks for using the calculator!!')
                break

        op = input('Choose operation [/ * - + c s]: ').strip().lower()
        if op == 's':
            print('\nThanks for using the calculator!!')
            break
        elif op == 'c':
            history.clear()
            print('History cleared.\n')
            current = None
            continue
        elif op not in ('/', '*', '-', '+'):
            print('Choose only the referred options!!')
            continue

        next_val = get_number('Enter the next value: ')
        if next_val is None:
            print('\nThanks for using the calculator!!')
            break

        if op == '/':
            if next_val == 0:
                print('Cannot divide by zero!')
                continue
            current = current / next_val
        elif op == '*':
            current = current * next_val
        elif op == '-':
            current = current - next_val
        elif op == '+':
            current = current + next_val

        history.append(current)
        print(f'Result = {current:.2f}')
        print_history(history)
        print()  # Newline for better readability

if __name__ == "__main__":
    main()
