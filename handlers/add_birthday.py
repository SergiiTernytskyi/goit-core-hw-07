from colorama import Fore
from handlers.input_error import input_error


@input_error
def add_birthday(args, book):
    """
    Add birthday date to contact record in adress book.
        
    Parameters:
        args: includes name and birthday of contact.
        book (AdressBook): adress book instance.
    """
    name, birthday, *_ = args
    record = book.find(name)
    record.add_birthday(birthday)
    return f"{Fore.GREEN}Contact birthday updated.{Fore.RESET}"