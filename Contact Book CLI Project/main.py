import json
import os

class Contact:
    def __init__(self, name, phone, email, adress):
        self.name = name
        self.phone = phone
        self.email = email
        self.adress = adress

    def to_dict(self):
        return {
            "Name": self.name,
            "Phone": self.phone,
            "Email": self.email,
            "Adress": self.adress
        }
    @classmethod
    def from_dict(cls, data):
        print("New contact object Created")
        return cls(
            name = data["name"],
            phone = data["phone"],
            email = data["email"],
            adress = data["adress"]
        )


class ContactBook:
    def __init__(self, name):
        self.bookName = f"{name}.json"


    def load_from_files(self):
        if os.path.exists(self.bookName):
            with open(self.bookName, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if not content:
                    return []
                try:
                    contacts = json.loads(content)
                except json.JSONDecodeError:
                    print(f"Warning: {self.bookName} is not valid JSON. Starting with an empty contact list.")
                    return []
        else:
                contacts = []
        return contacts
    

    def save_to_file(self, contacts_list):
        if not contacts_list:
            print("contacts Is Empty")
            return

        with open(self.bookName, 'w', encoding='utf-8') as f:
            json.dump(contacts_list, f, indent=2)
            print(f"{len(contacts_list)} Contacts saved to {self.bookName}")


    def add_contact(self,new_contact):
        name = new_contact.get("Name")
        phone = new_contact.get("Phone")
        email = new_contact.get("Email")
        adress = new_contact.get("Adress")

        print(f"New Contact Created:\nName: {name}\nPhone: {phone}\nEmail: {email}\nAddress: {adress}")

        contacts = self.load_from_files()
        
        for con in contacts:
            if phone == con["Phone"]:
                print("Contact Already Existed...")
                return
        contacts.append(new_contact)
        print(f"Contact adeed to {self.bookName}")

        self.save_to_file(contacts_list=contacts)


    def search_contact(self, keyWord, value):
        print("\nSearching for a contact.....")
        contacts = self.load_from_files()
        datas = []

        for dt in contacts:
            if keyWord in dt.keys() and value == dt[keyWord]:
                print("Contact Founded.")
                datas.append(dt)

        if not datas:
            print("Contact Not Founded....")
        else:
            print()
            for data in datas:
                name = data.get("Name")
                print("Name:", name)
                phone = data.get("Phone")
                print("Phone Number:", phone)
                email = data.get("Email")
                print("Email:", email)
                adress = data.get("Adress")
                print("Adress:", adress)
                print()

            return
    

    def delete_contact(self, name,number):
        print("\nDeleting a contact......")
        contacts = self.load_from_files()

        for contact in contacts:
            if name == contact["Name"] and number == contact["Phone"]:
                scarificial_lamb = contact

                contacts.remove(scarificial_lamb)
                print("A contact has been removed.")
                print(scarificial_lamb)

                self.save_to_file(contacts_list=contacts)

                return
        
        print("This contact doesn't exists...")


    def modify_contact(self, name, number, keyword, new_value):
        contacts = self.load_from_files()

        for i in range(len(contacts)):
            if name == contacts[i]["Name"] and number == contacts[i]["Phone"]:
                old_value = contacts[i][keyword]
                contacts[i][keyword] = new_value

                print(f'{keyword} modified of Name: {contacts[i]["Name"]}\nPhone: {contacts[i]["Phone"]}')
                print(f"Modified: {old_value} --> {new_value}")
                return
            
        print("Contact not found.....")
                
            
    def view_contacts(self):
        print("\nViewing all contacts...........")
        contacts = self.load_from_files()
        for contact in contacts:
            print(f"Name: {contact["Name"]}")
            print(f"Phone: {contact["Phone"]}")
            print(f"Email: {contact["Email"]}")
            print(f"Adress: {contact["Adress"]}")
            print()

        

if __name__ == "__main__":
    book = ContactBook("Yoo")

    cont1 = {
        "name": "Rejuwan",
        "phone": "0190000",
        "email": "rt.jeion@gmail.com",
        "adress": "Gazipur"
    }

    cont2 = {
        "name": input("Name: "),
        "phone": input("Phone: "),
        "email": input("Email: "),
        "adress": input("Adress: ")
    }
    contact1 = Contact("RT Jeion", "019000000", "rt.jeion@gmail.com", "Gazipur, Dhaka")
    contact2 = Contact.from_dict(cont1)
    contact3 = Contact("RT Jeion", "019000012", "rt.jeion@gmail.com", "Gazipur, Dhaka")
    contact4 = Contact.from_dict(cont2)

    book.search_contact("Name", "RT Jeion")
    book.add_contact(contact4.to_dict())
