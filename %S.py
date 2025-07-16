# List of users who purchased
users = [
    {'name': 'Ana', 'age': 28, 'product': 'Keyboard', 'quantity': 2, 'price': 89.90},
    {'name': 'Bruno', 'age': 34, 'product': 'Mouse', 'quantity': 1, 'price': 49.90},
    {'name': 'Carlos', 'age': 22, 'product': 'Monitor', 'quantity': 1, 'price': 999.99},
]

print('PURCHASE REPORT\n')

# Formatted display using %s
for user in users:
    message = 'Hello, %s! You are %s years old.' % (user['name'], user['age'])
    report = 'Product: %s | Quantity: %s | Unit price: $%s' % (user['product'], user['quantity'], user['price'])

    print(message)
    print(report)
    print('-' * 40)

