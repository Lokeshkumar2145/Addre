from addressbook import AddressBook
from contact import Contact

class AddressBookMain:
    def __init__(self):
        self.address_book = AddressBook()

    def add_contact_console(self):
        print("\nEnter Contact Details:")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        address = input("Address: ")
        city = input("City: ")
        state = input("State: ")
        zip_code = input("ZIP Code: ")
        phone_number = input("Phone Number: ")
        email = input("Email: ")

        new_contact = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
        self.address_book.add_contact(new_contact)

    def edit_contact_console(self):
        print("\nEnter Details of the Contact to be Edited of Existing contact of first name:")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        address = input("Address: ")
        city = input("City: ")
        state = input("State: ")
        zip_code = input("ZIP Code: ")
        phone_number = input("Phone Number: ")
        email = input("Email: ")

        updated_contact=Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
        self.address_book.edit_contact(first_name, updated_contact)
        print("\nContacts Edited successfully !!")


    def display_menu(self):
        while True:
            print("\n=== Address Book Menu ===")
            print("1. Add Contact")
            print("2. Edit Contact")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_contact_console()
            elif choice == "2":
                self.edit_contact_console()
            elif choice == "3":
                print("Exiting Address Book. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = AddressBookMain()
    app.display_menu()
