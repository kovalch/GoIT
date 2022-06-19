from collections import UserDict
from datetime import datetime, date

class Field:

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


class Name(Field):
    pass


class Phone(Field):

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        if value[0] != '+':
            raise ValueError("Phone number must starts from +")
        elif len(value[1:]) != 12:
            raise ValueError("Phone number must contain exactly 12 digits")
        self.__value = value


class Birthday(Field):

    @property
    def value(self) -> datetime:
        return self.__value

    @value.setter
    def value(self, value):
        try:
            self.__value = datetime.strptime(value, '%d %B, %Y').date()
        except (TypeError, ValueError):
            raise ValueError("Please give a date in a way: '%d %B, %Y'")


class Record:

    def __init__(self, name, phone = None, birthday = None):

        self.name = name
        print(f"Add a new contact with a name {self.name}")
        if phone is None:
            self.phone = []
        else:
            self.phone = [phone]
            print(f"and a phone number {self.phone}")
        self.birthday = birthday
        print(f"and a birthday on {self.birthday}")

    # Phone number methods
    def add_phone_number(self, phone_number):

        if phone_number not in self.phone:
            print(f"Adding new phone number: {phone_number}")
            self.phone.append(phone_number)

    def find_phone_number(self, phone_number):

        for i in self.phone:
            if i == phone_number:
                print(f"{i} number was found")
                return i
        print("Cannot find a given phone number")

    def delete_phone_number(self, phone_number):

        phone_number_to_delete = self.find_phone_number(phone_number)
        if phone_number_to_delete:
            print(f"{phone_number_to_delete} number are going to be deleted")
            self.phone.remove(phone_number_to_delete)

    def edit_phone_number(self, phone_number, new_phone_number):

        phone_number_to_edit = self.find_phone_number(phone_number)
        if phone_number_to_edit:
            self.phone.remove(phone_number_to_edit)
            self.phone.append(new_phone_number)
            print(f"{phone_number_to_edit} number was changed to {new_phone_number}")

    def days_to_birthday(self):

        if self.birthday:
            birthday_value = self.birthday.value
            today = date.today()
            try:
                birthday_this_year = birthday_value.replace(year=today.year)
                delta_days = (birthday_this_year - today).days
                print("Number of days till the next birthday:")
                return delta_days
            except ValueError:
                birthday_this_year = birthday_value.replace(year=today.year, day=28)
                delta_days = (birthday_this_year - today).days
                print("Number of days till the next birthday:")
                return delta_days
            print("No birthday was given")


class AddressBook(UserDict):

    def add_record(self, record: list):
        self.data[record.name.value] = record

    def iterator(self, n):
        self.n = n
        print(f"There will be shown only first {n} records")
        self.count = 0

    def __next__(self):

        dict_to_return = []
        self.count += 1

        for key, value in self.data.items():
            dict_to_return.append((key, value))

            if len(dict_to_return) == self.n:
                break

        if self.count == self.n+1:
            raise StopIteration

        return dict_to_return

    def __iter__(self):
        return self




name = Name("Bill")
name2 = Name("Niko")
name3 = Name("Zen")

phone = Phone("+380958478343")
phone2 = Phone("+380945343256")
phone3 = Phone("+380945343555")

birthday = Birthday("25 October, 1990")
birthday2 = Birthday("03 June, 2006")

rec = Record(name, phone, birthday)
print(rec.days_to_birthday())

rec2 = Record(name2, phone2, birthday2)
rec3 = Record(name3, phone3)

rec.add_phone_number(phone2)
rec.edit_phone_number(phone2,phone3)
rec.add_phone_number(phone2)
print(rec.phone)
rec.delete_phone_number(phone)
print(rec.phone)

ab = AddressBook()
ab.add_record(rec)
ab.add_record(rec2)
ab.add_record(rec3)
print(ab)

ab_iterable = ab.iterator(2)

for i in ab:
    print(i)

