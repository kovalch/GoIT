from collections import UserDict


class Field:

    def __init__(self, value):
        self.value = value


class Name(Field):
    def value(self):
        return self.__value


class Phone(Field):

    def value(self):
        return self.__value


class Record:

    def __init__(self, name, phone = None):
        self.name = Name(name)
        print(f"Add a new contact with a name {self.name.value}")
        if phone is None:
            self.phone = []
        else:
            self.phone = [Phone(p).value for p in phone]
            print(f"and a phone number {self.phone}")

    def add_phone_number(self, phone_number):
        phone = Phone(phone_number).value
        if phone not in self.phone:
            print(f"Adding new phone number: {phone}")
            self.phone.append(phone)

    def find_phone_number(self, phone_number):
        phone = Phone(phone_number).value
        for i in self.phone:
            if i == phone:
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
        new_phone = Phone(new_phone_number).value
        if phone_number_to_edit in self.phone:
            self.phone.remove(phone_number_to_edit)
            self.phone.append(new_phone)
            print(f"{phone_number_to_edit} number was changed to {new_phone}")


class AddressBook(UserDict):

    def add_record(self, record):
        new_record = Record(record[0], record[1:])
        self.data[new_record.name.value] = new_record


phone_book_1 = AddressBook()
record = ['Nata', "+3809453432"]
record2 = ['Oleg', "3434"]
phone_book_1.add_record(record)
phone_book_1.add_record(record2)
phone_book_1[record[0]].add_phone_number("2334")
phone_book_1[record[0]].add_phone_number("32434345")
print(phone_book_1[record[0]].find_phone_number("2334"))
print(phone_book_1[record[0]].edit_phone_number("2334","44444"))
phone_book_1[record[0]].delete_phone_number("2334")
