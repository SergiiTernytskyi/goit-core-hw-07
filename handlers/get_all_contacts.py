from colorama import Fore
from handlers.input_error import input_error


@input_error
def get_all_contacts(book):
    """
    Return contacts list from adress book.
        
    Parameters:
        book (AdressBook): adress book instance.
    """
    contacts_list = []
    for field in book:
        user = book.get(field)
        contacts_list.append(f"{Fore.GREEN}{user}{Fore.RESET}")

    if contacts_list:
        return '\n'.join(contacts_list)
    else:
        return f"{Fore.GREEN}There are no contacts in Adress book yet.{Fore.RESET}"