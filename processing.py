from colorama import Fore
from input_error import input_error


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"{Fore.GREEN}Contact added.{Fore.RESET}"


@input_error
def get_all_contacts(contacts):    
    if(contacts.keys()):
        contacts_list = []
        for contact in contacts:
            contacts_list.append(f"{Fore.GREEN}{contact}: {contacts[contact]}{Fore.RESET}")

        return '\n'.join(contacts_list)
    else:
        return f"{Fore.RED}Oops! There is no contacts.{Fore.RESET}"


@input_error 
def get_contact(args, contacts):    
    name = args[0]        
    return f"{Fore.GREEN}Phone number for {name} is {contacts[name]}{Fore.RESET}"


@input_error
def change_contact(args, contacts):   
    name, phone = args
    contacts[name] = phone
    return f"{Fore.GREEN}Contact changed.{Fore.RESET}"
