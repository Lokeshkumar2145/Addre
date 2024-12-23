from addressbook import AddressBook
from contact import Contact

class AddressBookSystem:
    def __init__(self):
        self.address_books = {}

    def add_address_book(self):
        name = input("\nEnter a unique name for the new Address Book: ").strip()
        if name in self.address_books:
            print(f"Address Book with the name '{name}' already exists.")
        else:
            self.address_books[name] = AddressBook()
            print(f"Address Book '{name}' added successfully.")

    def select_address_book(self):
        if not self.address_books:
            print("\nNo Address Books available. Please create one first.")
            return None
        print("\nAvailable Address Books:")
        for id, name in enumerate(self.address_books.keys(), start=1):
            print(f"{id}. {name}")
        addressbookname = input("Select an Address Book by name: ").strip()
        if addressbookname in self.address_books:
            return self.address_books[addressbookname]
        else:
            print("Invalid Address Book name. Please try again.")
            return None

    def manage_address_book(self):
        address_book = self.select_address_book()
        if not address_book:
            return
        while True:
            print("\n=== Manage Selected Address Book ===")
            print("1. Add Contact")
            print("2. Edit Contact")
            print("3. Delete Contact")
            print("4. View All Contacts")
            print("5. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_contacts_to_book(address_book)
            elif choice == "2":
                self.edit_contact_console(address_book)
            elif choice == "3":
                self.delete_contact_console(address_book)
            elif choice == "4":
                address_book.view_contacts()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

    def add_contacts_to_book(self, address_book):
        while True:
            print("\nEnter details for a new contact:")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            address = input("Address: ")
            city = input("City: ")
            state = input("State: ")
            zip_code = input("ZIP Code: ")
            phone_number = input("Phone Number: ")
            email = input("Email: ")

            new_contact = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
            address_book.add_contact(new_contact)

            another = input("Do you want to add another contact? (yes/no): ").strip().lower()
            if another != "yes":
                break

    def edit_contact_console(self, address_book):
        first_name = input("\nEnter the first name of the contact to edit: ")
        print("\nEnter updated details:")
        last_name = input("Last Name: ")
        address = input("Address: ")
        city = input("City: ")
        state = input("State: ")
        zip_code = input("ZIP Code: ")
        phone_number = input("Phone Number: ")
        email = input("Email: ")

        updated_contact = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
        success = address_book.edit_contact(first_name, updated_contact)

        if success:
            print("\nContact updated successfully!")
        else:
            print("\nContact not found.")

    def delete_contact_console(self, address_book):
        first_name = input("\nEnter the first name of the contact to delete: ")
        success = address_book.delete_contact(first_name)

        if success:
            print("\nContact deleted successfully!")
        else:
            print("\nContact not found.")

    def view_all_address_books(self):
        if not self.address_books:
            print("\nNo Address Books available.")
        else:
            print("\nAvailable Address Books:")
            for name in self.address_books.keys():
                print(f"- {name}")

    def search_person_across_books(self):
        search_city = input("\nEnter the city to search for contacts (leave blank to skip): ").strip()
        search_state = input("Enter the state to search for contacts (leave blank to skip): ").strip()

        results = []
        total_city_count = 0
        total_state_count = 0
        for name, address_book in self.address_books.items():
            matches, city_count, state_count = address_book.search_by_city_or_state(city=search_city, state=search_state)
            results.extend([(name, contact) for contact in matches])
            total_city_count += city_count
            total_state_count += state_count

        if results:
            print("\nSearch Results:")
            for book_name, contact in results:
                print(f"[Address Book: {book_name}] {contact}")
            
            if search_city:
                print(f"\nTotal contacts in city '{search_city}': {total_city_count}")
            if search_state:
                print(f"Total contacts in state '{search_state}': {total_state_count}")
        else:
            print("\nNo matching contacts found.")

    def display_menu(self):
        while True:
            print("\n=== Address Book System Menu ===")
            print("1. Add New Address Book")
            print("2. Manage Existing Address Book")
            print("3. Search Person across Address Book")
            print("4. View All Address Books")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_address_book()
            elif choice == "2":
                self.manage_address_book()
            elif choice == "3":
                self.search_person_across_books()
            elif choice == "4":
                self.view_all_address_books()
            elif choice == "5":
                print("Exiting Address Book System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = AddressBookSystem()
    app.display_menu()
