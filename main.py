from contact import Contact
from addressbook import AddressBook

# Create an AddressBook object
address_book = AddressBook()


# Add contacts
contact1 = Contact("lokesh", "kumar", "HSR", "Bangalore", "KA", "560102", "9876543211", "lokesh@gmail.com")
contact2 = Contact("ram", "mohan", "BTM", "Bangalore", "KA", "560068", "9876543210", "ram@gmail.com")
address_book.add_contact(contact1)
address_book.add_contact(contact2)

# View contacts
print("Contacts:")
address_book.view_contacts()

# Edit a contact
updated_contact = Contact("eran", "goud", "HSR", "Bangalore", "KA", "560069", "9123456789", "eran@gmail.com")
address_book.edit_contact("ram", updated_contact)

# View contacts after editing
print("\nUpdated Contacts:")
address_book.view_contacts()

# Delete a contact
address_book.delete_contact("eran")

# View contacts after deletion
print("\nContacts After Deletion:")
address_book.view_contacts()
