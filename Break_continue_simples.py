# Program to calculate the total number of products added by the user.

total = 0.0
product_count = 0


while True:
    user_input = input("Enter the price of the next product or press '1' to exit: ")

    if user_input.lower() == "1":
        print("Exiting...")
        break # Stop the loop

    try:
        price = float(user_input)
    except ValueError:
        print("Invalid value! Please enter a valid number or '1' to finish.")
    
    if price < 0:
        print("Negative prices are not allowed. Try again.")
        continue # Return to the beginning of the loop
    
    total += price
    product_count += 1
    print(f"Product {product_count} added. Currente total: ${total:.2f}")

    more = input("Do you want to add another product? [y/n]: ").strip().lower()
    if more == 'n' or more == "no":
        print("Finished adding product.")
        break
    elif more != 'y' and more != "yes":
        print("Invalid option! Assuming 'no'.")
        break

print(f"\nYou entered {product_count} products.")
print(f"The total value of the products is: ${total:.2f}")
