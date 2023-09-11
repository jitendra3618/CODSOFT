# Contact Book in Python

# Initialize an empty dictionary to store contacts
contacts = {}

# Function to add a contact
def add_contact(name, phone, email, address):
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print(f"Contact '{name}' added successfully.")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("Contact book is empty.")
    else:
        print("\nContacts:")
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print("-" * 20)

# Function to search for a contact by name or phone number
def search_contact(query):
    matching_contacts = []
    for name, details in contacts.items():
        if query in name or query in details['phone']:
            matching_contacts.append((name, details))
    return matching_contacts

# Function to update a contact
def update_contact(name, phone, email, address):
    if name in contacts:
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"Contact '{name}' not found.")

# Function to delete a contact
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

# Main loop
while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Quit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == '1':
        name = input("Enter the name: ")
        phone = input("Enter the phone number: ")
        email = input("Enter the email: ")
        address = input("Enter the address: ")
        add_contact(name, phone, email, address)
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        query = input("Enter a name or phone number to search: ")
        matching_contacts = search_contact(query)
        if matching_contacts:
            print("\nMatching Contacts:")
            for name, details in matching_contacts:
                print(f"Name: {name}")
                print(f"Phone: {details['phone']}")
                print(f"Email: {details['email']}")
                print(f"Address: {details['address']}")
                print("-" * 20)
        else:
            print("No matching contacts found.")
    elif choice == '4':
        name = input("Enter the name of the contact to update: ")
        phone = input("Enter the updated phone number: ")
        email = input("Enter the updated email: ")
        address = input("Enter the updated address: ")
        update_contact(name, phone, email, address)
    elif choice == '5':
        name = input("Enter the name of the contact to delete: ")
        delete_contact(name)
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
