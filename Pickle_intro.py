import pickle

def save_data(name: str, number: str, address: str) -> None:
    # Create a dictionary to save
    record = {
        'name': name,
        'number': number,
        'address': address
    }
    # Open the file in write-binary mode and save the dictionary
    with open('mydata.pkl', 'wb') as file:
        pickle.dump(record, file)

# Save a record
save_data('Leo', '1234', 'Alvaro Ramos Street')

# Open the file in read-binary mode and load the data
with open('mydata.pkl', 'rb') as file:
    loaded_record = pickle.load(file)
    print(loaded_record)
