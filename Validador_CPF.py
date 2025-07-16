# CPF Validator (Brazilian ID Number)

while True:
    cpf = input('Enter your CPF (only numbers, or with dots/dashes): ').strip()
    clean_cpf = ''
    # Remove dots and dashes
    for char in cpf:
        if char.isdigit():
            clean_cpf += char

    if len(clean_cpf) != 11:
        print("CPF must have 11 digits.")
        continue

    original_cpf = clean_cpf
    cpf_base = clean_cpf[:-2]
    reverso = 10
    total = 0

    # Generate the two verifying digits
    for i in range(19):
        if i > 8:
            i -= 9
        total += int(cpf_base[i]) * reverso
        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)
            if d > 9:
                d = 0
            total = 0
            cpf_base += str(d)

    if cpf_base == original_cpf:
        print('CPF is valid.')
        break
    else:
        print('Invalid CPF.')
