from colorama import Fore
from say_hello import say_hello
from parse_input import parse_input
from processing import add_contact, get_all_contacts, get_contact, change_contact

def main():
    print(f"{Fore.BLUE}Welcome to the assistant bot! {Fore.RESET}")
    
    name = input(f"{Fore.YELLOW}Enter Your name: {Fore.RESET}")
    print(say_hello(name))

    contacts = {}

    while True:
        user_input = input(f"{Fore.YELLOW}Enter a command: {Fore.RESET}").strip().lower()
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(f"{Fore.GREEN}Good bye!{Fore.RESET}")
        elif command == "hello":
            print(f"{Fore.GREEN}How can I help you?{Fore.RESET}")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_contact(args, contacts))
        elif command == "all":
            print(get_all_contacts(contacts))
        else:
            print(f"{Fore.RED}Invalid command. Try again...{Fore.RESET}")


if __name__ == "__main__":
    main()