from collections import defaultdict
from operator import attrgetter
import json
from contact import Contact


class AddressBook:
    def __init__(self):
        self.city_map = defaultdict(list)
        self.state_map = defaultdict(list)
        self.contacts = []

    def is_duplicate(self, first_name, last_name):
        return any(contact.first_name == first_name and contact.last_name == last_name for contact in self.contacts)

    def add_contact(self, contact):
        if self.is_duplicate(contact.first_name, contact.last_name):
            print(f"Duplicate entry: {contact.first_name} {contact.last_name} already exists.")
            return False
        self.contacts.append(contact)
        self.city_map[contact.city].append(contact)
        self.state_map[contact.state].append(contact)
        print(f"Contact added successfully: {contact}")
        return True
        
    def edit_contact(self, first_name, updated_contact):
        for index, contact in enumerate(self.contacts):
            if contact.first_name == first_name:
                self.contacts[index] = updated_contact
                old_city = contact.city
                old_state = contact.state
                self.contacts[index] = updated_contact
                self.city_map[old_city].remove(contact)
                self.state_map[old_state].remove(contact)
                self.city_map[updated_contact.city].append(updated_contact)
                self.state_map[updated_contact.state].append(updated_contact)
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
        results = []
        city_count = 0
        state_count = 0

        if city:
            city_contacts = self.city_map.get(city, [])
            results.extend(city_contacts)
            city_count = len(city_contacts)
        
        if state:
            state_contacts = self.state_map.get(state, [])
            results.extend(state_contacts)
            state_count = len(state_contacts)
        
        return results, city_count, state_count

    def sort_contacts_by_name(self):
        if not self.contacts:
            print("No contacts available to sort.")
        else:
            # Sort contacts alphabetically by first and last name
            sorted_contacts = sorted(self.contacts, key=attrgetter('first_name', 'last_name'))
            print("\nContacts sorted alphabetically by name:")
            for contact in sorted_contacts:
                print(contact)
        def save_to_file(self, file_name):
            try:
                with open(file_name, 'w') as file:
                    # Convert contact objects to dictionaries and write to file
                    json.dump([contact.__dict__ for contact in self.contacts], file, indent=4)
                print(f"Address book saved to {file_name}")
            except Exception as e:
                print(f"Error saving address book: {e}")

    def load_from_file(self, file_name):
        try:
            with open(file_name, 'r') as file:
                # Load JSON data and recreate contact objects
                data = json.load(file)
                self.contacts = [Contact(**contact_data) for contact_data in data]
            print(f"Address book loaded from {file_name}")
        except FileNotFoundError:
            print(f"File {file_name} not found. Starting with an empty address book.")
        except Exception as e:
            print(f"Error loading address book: {e}")