# 'continues' is a flag variable; if 'y' is entered, the loop continues
continues = 'y'
total = 0.0  # Will accumulate the sum of product prices

while continues == 'y':
    price = float(input('Enter the price of the next product: '))
    total += price
    continues = input('Do you want to add more products? [y/n]: ').strip().lower()
    print('The total value of the products is: $%.2f' % total)
