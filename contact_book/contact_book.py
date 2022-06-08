phone_book = [
    {
        "name":"Bill",
        "phone_number": "80957469332"
    },
    {
        "name":"Giil",
        "phone_number": "+380567395645"
    },
    {
        "name":"Till",
        "phone_number": "01377395645"
    },
    {
        "name": "Nora",
        "phone_number": " 01377395645"
    }
]

def input_error(func):
    def inner_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            if func.__name__ == "add":
                print("Give me the name and the phone number please")
            elif func.__name__ == "change":
                print(f"Give me the name and the NEW phone number please")
            elif func.__name__ == "phone":
                print(f"Enter user name please")
    return inner_function


def start(start_word=""):
    if start_word == "hello":
        return print("How can I help you?")

@input_error
def add(name, phone_number, phone_book=phone_book):
    phone_contact = {}
    phone_contact["name"] = name
    phone_contact["phone_number"] = phone_number
    phone_book.append(phone_contact)
    return phone_book

@input_error
def change(name, phone_number, phone_book=phone_book):
    for phone_contact in phone_book:
        if phone_contact["name"].casefold() == name:
            phone_contact["phone_number"] = phone_number
            return phone_book
    return print(f"There is no such a name: {name}")
        
@input_error
def phone(name, phone_book=phone_book):
    for phone_contact in phone_book:
        if phone_contact["name"].casefold() == name:
            return print(phone_contact["phone_number"])
    return print(f"There is no such a name: {name}")

def show_all():
    for phone_contact in phone_book:
        print('{:^10} {:^10}'.format(phone_contact["name"], phone_contact["phone_number"]))
    return

def stop(stop_word=""):
    if stop_word in ["good bye", "close", "exit"]:
        return print("Good bye!")

operations = {"hello":start, "add":add, "change":change, "phone":phone,
              "show all":show_all, "close":stop, "exit":stop, "good bye":stop}


def operate(operator):
    return operations[operator]

command_list = []
for k in operations.keys():
    command_list.append(k)


def main(command_list=command_list):
    input_number = 1
    while input_number > 0:
      command_line = input("").casefold()
      if command_line == ".":
          break

      all_words = command_line.split()
      try: 
          if len(all_words) == 1 and command_line in command_list:
            operate(command_line)(command_line)
          elif len(all_words) == 2:
              try:
                operate(command_line)(command_line)
              except TypeError:
                operate(command_line)()
              except:
                operate(all_words[0])(all_words[1])
          elif len(all_words) == 3:
            operate(all_words[0])(all_words[1], all_words[2])
          else:
            print(f"There is no such a command: {command_line}")
            print(f"Please use one of the existing commands: {command_list}")
      except KeyError:
          print(f"There is no such a command: {command_line}")
          print(f"Please use one of the existing commands: {command_list}")

      if command_line in ["good bye", "close", "exit"]:
        break

      input_number += 1

main(command_list)
