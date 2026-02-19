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

    def add_contact(self,name, phone, email, adress):
        contact = Contact(name, phone, email, adress)
        print(f"New Contact Created:\nName: {name}\nPhone: {phone}\nEmail: {email}\nAddress: {adress}")
        if os.path.exists(self.bookName):
            with open(self.bookName) as f:
                contacts = json.load(f)
        else:
                contacts = []

        contacts.append(contact.to_dict())
        print(f"Contact adeed to {self.bookName}")
        return contacts

    def search_contact(self, keyWord):
        if not os.path.exists(self.bookName):
            print("There is not ContactBook")
            return

        with open(self.bookName, 'r') as f:
            contacts = json.loaf(f)

        for data in contacts:
            if keyWord in data.keys():
                print("Contact Founded.")
                return data
        return "Contact Nof Found"

if __name__ == "__main__":
    contact1 = Contact("RT Jeion", "019000000", "rt.jeion@gmail.com", "Gazipur, Dhaka")
    con = {
        "name": "Rejuwan",
        "phone": "0190000",
        "email": "rt.jeion@gmail.com",
        "adress": "Gazipur"
    }
    contact2 = Contact.from_dict(con)
print(contact1.to_dict())

print(contact2.to_dict())
