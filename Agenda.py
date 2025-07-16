contacts = []

def clear_screen():
    # Simulate clearing the screen by printing many blank lines
    print('\n' * 40)

def menu():
    # Display menu and get user's option
    clear_screen()
    print('Contacts Agenda - Select an option:')
    print('[1] Add Contact')
    print('[2] Edit Contact')
    print('[3] Delete Contact')
    print('[4] Find by Name')
    print('[5] List All Contacts')
    print('[6] Exit')
    choice = input('Your choice: ')
    # Return the selected option as integer, or 0 if not a number
    return int(choice) if choice.isdigit() else 0

def create_contact():
    # Get contact data from user and return as a dictionary
    clear_screen()
    name = input('Enter contact name: ')
    phone = input('Enter contact phone: ')
    return {'name': name, 'phone': phone}

def find_index_by_name(name):
    # Search for a contact by name and return its index, or -1 if not found
    for idx, contact in enumerate(contacts):
        if contact['name'].lower() == name.lower():
            return idx
    return -1

def add_contact():
    # Add a new contact to the agenda
    contact = create_contact()
    contacts.append(contact)
    input('Contact added. Press <enter>...')

def edit_contact():
    # Edit a contact's phone number
    name = input('Enter the name of the contact to edit: ')
    idx = find_index_by_name(name)
    if idx != -1:
        print(f"Editing contact: {contacts[idx]['name']} - {contacts[idx]['phone']}")
        new_phone = input('Enter the new phone number: ')
        contacts[idx]['phone'] = new_phone
        input('Contact updated. Press <enter>...')
    else:
        input('Contact not found. Press <enter>...')

def delete_contact():
    # Delete a contact from the agenda
    name = input('Enter the name of the contact to delete: ')
    idx = find_index_by_name(name)
    clear_screen()
    if idx != -1:
        removed = contacts.pop(idx)  # Remove the contact from the list
        print(f'Removed contact: {removed["name"]} - {removed["phone"]}')
        input('Press <enter>...')
    else:
        input('Contact not found. Press <enter>...')

def find_contact_by_name():
    # Display a contact by name
    name = input('Enter the contact name to find: ')
    idx = find_index_by_name(name)
    clear_screen()
    if idx != -1:
        print(f'Contact found:\nName: {contacts[idx]["name"]} - Phone: {contacts[idx]["phone"]}')
    else:
        print('Contact not found.')
    input('Press <enter>...')

def list_contacts():
    # List all contacts
    clear_screen()
    if not contacts:
        print('No contacts registered.')
    else:
        print('Contacts list:')
        for c in contacts:
            print(f'Name: {c["name"]} - Phone: {c["phone"]}')
    input('Press <enter> to return to the menu...')

# Main program loop
option = 0
while option != 6:
    option = menu()
    if option == 1:
        add_contact()
    elif option == 2:
        edit_contact()
    elif option == 3:
        delete_contact()
    elif option == 4:
        find_contact_by_name()
    elif option == 5:
        list_contacts()
    elif option == 6:
        break
    else:
        # Handle invalid option
        input('Invalid option. Press <enter>...')
print('Session ended by the user.')
