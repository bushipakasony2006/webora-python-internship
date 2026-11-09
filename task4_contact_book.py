contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")

    contacts[name] = phone
    print("Contact added successfully!")

def view_contacts():
    if len(contacts) == 0:
        print("Your contact book is empty.")
    else:
        print("\n===== CONTACT LIST =====")
        for name, phone in contacts.items():
            print("Name:", name, "| Phone:", phone)

def search_contact():
    name = input("Enter name to search: ")

    if name in contacts:
        print("Contact found!")
        print("Name:", name)
        print("Phone:", contacts[name])
    else:
        print("Contact not found!")

while True:
    print("\n===== CONTACT BOOK MENU =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        print("Thank you for using Contact Book!")
        break
    else:
        print("Invalid choice! Please select 1 to 4.")
