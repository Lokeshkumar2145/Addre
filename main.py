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

    def display_menu(self):
        while True:
            print("\n=== Address Book Menu ===")
            print("1. Add Contact")
            print("2. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_contact_console()
            elif choice == "2":
                print("Exiting Address Book. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = AddressBookMain()
    app.display_menu()
