class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact added successfully: {contact}")
        
    def edit_contact(self, first_name, updated_contact):
        for index, contact in enumerate(self.contacts):
            if contact.first_name == first_name:
                self.contacts[index] = updated_contact
                return True
        return False
    
    def delete_contact(self, first_name):
        for contact in self.contacts:
            if contact.first_name == first_name:
                self.contacts.remove(contact)
                return True
        return False

