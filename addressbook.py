class AddressBook:
    def __init__(self):
        self.contacts = []

    def is_duplicate(self, first_name, last_name):
        return any(contact.first_name == first_name and contact.last_name == last_name for contact in self.contacts)

    def add_contact(self, contact):
        if self.is_duplicate(contact.first_name, contact.last_name):
            print(f"Duplicate entry: {contact.first_name} {contact.last_name} already exists.")
            return False
        self.contacts.append(contact)
        print(f"Contact added successfully: {contact}")
        return True
        
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
    
    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                print(contact)
    
    def search_by_city_or_state(self, city=None, state=None):
        results = [contact for contact in self.contacts if (city and contact.city == city) or (state and contact.state == state)] #list comprehension
        return results

