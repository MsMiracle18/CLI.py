contacts = {}


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input. Please enter name and phone number separated by a space."
        except IndexError:
            return "Invalid input. Please enter a command."
    return inner


@input_error
def add_contact(contact_info):
    name, phone = contact_info.split()
    contacts[name] = phone
    return "Contact added successfully."


@input_error
def change_phone(contact_info):
    name, phone = contact_info.split()
    contacts[name] = phone
    return "Phone number changed successfully."


@input_error
def get_phone(name):
    return contacts[name]


def show_all_contacts():
    if not contacts:
        return "No contacts found."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result


def main():
    while True:
        command = input("Enter a command: ").lower()
        if command == "hello":
            print("How can I help you?")
        elif command.startswith("add"):
            contact_info = input("Enter name and phone number: ")
            print(add_contact(contact_info))
        elif command.startswith("change"):
            contact_info = input("Enter name and new phone number: ")
            print(change_phone(contact_info))
        elif command.startswith("phone"):
            name = input("Enter contact name: ")
            print(get_phone(name))
        elif command == "show all":
            print(show_all_contacts())
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
