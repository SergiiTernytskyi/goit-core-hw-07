from colorama import Fore
from handlers.input_error import input_error
from classes import Record


@input_error
def add_contact(args, book):
    """
    Add contact and updating contact in adress book.
        
    Parameters:
        args: includes name and phone number of contact.
        book (AdressBook): adress book instance.
    """
    name, phone, *_ = args
    record = book.find(name)
    message = f"{Fore.GREEN}Contact updated.{Fore.RESET}"

    if record == None:
        record = Record(name)
        book.add_record(record)
        message = f"{Fore.GREEN}Contact added.{Fore.RESET}"
    if phone:
        record.add_phone(phone)

    return message
