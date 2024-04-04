from colorama import Fore
from say_hello import say_hello
from parse_input import parse_input
from handlers.add_contact import add_contact
from handlers.get_contact import get_contact
from handlers.add_birthday import add_birthday
from handlers.show_birthday import show_birthday
from handlers.get_all_contacts import get_all_contacts
from handlers.birthdays_list import birthdays_list
from classes import AddressBook

def main():
    print(f"{Fore.BLUE}Welcome to the assistant bot! {Fore.RESET}")
    
    name = input(f"{Fore.YELLOW}Enter Your name: {Fore.RESET}")
    print(say_hello(name))

    book = AddressBook()

    while True:
        user_input = input(f"{Fore.YELLOW}Enter a command: {Fore.RESET}")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(f"{Fore.GREEN}Good bye!{Fore.RESET}")
            break
        elif command == "hello":
            print(f"{Fore.GREEN}Hello. How can I help you?{Fore.RESET}")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(add_contact(args, book))
        elif command == "phone":
            print(get_contact(args, book))
        elif command == "all":
            print(get_all_contacts(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))            
        elif command == "show-birthday":
            print(show_birthday(args, book))            
        elif command == "birthdays":
            print(birthdays_list(book))            
        else:
            print(f"{Fore.RED}Invalid command. Try again...{Fore.RESET}")


if __name__ == "__main__":
    main()