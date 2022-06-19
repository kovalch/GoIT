from collections import UserDict


class Field:

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name, phone = None):
        self.name = name
        print(f"Add a new contact with a name {self.name}")
        if phone is None:
            self.phone = []
        else:
            self.phone = [phone]
            print(f"and a phone number {self.phone}")

    def add_phone_number(self, phone_number):
        if phone_number not in self.phone:
            print(f"Adding new phone number: {phone_number}")
            self.phone.append(phone_number)

    def find_phone_number(self, phone_number):
        for i in self.phone:
            if i == phone_number:
                print(f"{i} number was found")
                return i
            else:
                print("Cannot find a given phone number")

    def delete_phone_number(self, phone_number):
        phone_number_to_delete = self.find_phone_number(phone_number)
        if phone_number_to_delete in self.phone:
            print(f"{phone_number_to_delete} number are going to be deleted")
            self.phone.remove(phone_number_to_delete)

    def edit_phone_number(self, phone_number, new_phone_number):
        phone_number_to_edit = self.find_phone_number(phone_number)
        new_phone = Phone(new_phone_number)
        if phone_number_to_edit in self.phone:
            self.phone.remove(phone_number_to_edit)
            self.phone.append(new_phone)
            print(f"{phone_number_to_edit} number was changed to {new_phone}")


class AddressBook(UserDict):

    def add_record(self, record: list):
        self.data[record.name.value] = record



name = Name("Bill")
phone = Phone("12345")
rec = Record(name, phone)
rec.add_phone_number("343434")
rec.find_phone_number("343434")
rec.edit_phone_number("343434","555555")
rec.add_phone_number("343434")
print(rec.phone)
ab = AddressBook()
ab.add_record(rec)


