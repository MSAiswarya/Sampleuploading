import pickle

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        print("NAME",self.name)
        print("PHONE",self.phone) 
        print("EMAIL",self.email) 

class ContactManager:
    def __init__(self, filename='contacts.pkl'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return []

    def save_contacts(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self.contacts, file)

    def add_contact(self, name, phone, email):
        self.contacts.append(Contact(name, phone, email))
        self.save_contacts()

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        for contact in self.contacts:
            print(contact)

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]
        self.save_contacts()

def main():
    manager = ContactManager()

    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            manager.add_contact(name, phone, email)
            print("Contact added successfully.")
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            name = input("Enter the name of the contact to delete: ")
            manager.delete_contact(name)
            print("Contact deleted successfully.")
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
