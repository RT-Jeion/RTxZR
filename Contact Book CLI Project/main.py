import json
import os

class Contact:
    def __init__(self, name, phone, email, adress):
        self.name = name
        self.phone = phone
        self.email = email
        self.adress = adress

    def to_dict():
        return {
            "Name": self.name,
            "Phone": self.phone,
            "Email": self.email,
            "Adress": self.adress
        }
    @classmethod
    def from_dict(cls, data):
        return cls(
            name = data["name"],
            phone = data["phone"],
            email = data["email"],
            adress = data["adress"]
        )


Class ContactBook:
    def __init__(self, name):
        self.bookName = f"{name}.json"

    def add_contact(self,name, phone, email, adress):
        contact = Contact(name, phone, email, adress)
        
        if os.path.exists(self.bookName):
            with open(self.bookName) as f:
                contacts = json.load(f)
            else:
                contacts = []

        contacts.append(contact.to_dict())
        return contacts

    def search_contact(self, keyWord):
        if not os.path.exists(self.bookName):
            print("There is not ContactBook")
            return

        with open(self.bookName, 'r') as f:
            contacts = json.loaf(f)

        for data in contacts:
            if keyWord in data.keys():
                return data
        return "Contact Nof Found"
