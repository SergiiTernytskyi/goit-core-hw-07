from colorama import Fore
from handlers.input_error import input_error


@input_error
def show_birthday(args, book):
    """
    Show birthday date to contact in adress book by name.
        
    Parameters:
        args: includes name of contact.
        book (AdressBook): adress book instance.
    """
    name = args[0]
    record = book.find(name)
    return f"{Fore.GREEN}{record['name']} birthday is on {record['birthday']}{Fore.RESET}"