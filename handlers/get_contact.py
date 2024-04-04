from colorama import Fore
from handlers.input_error import input_error


@input_error 
def get_contact(args, book):
    """
    Return contact by name from adress book.
        
    Parameters:
        args: includes contact name.
        book (AdressBook): adress book instance.
    """    
    name = args[0]
    
    record = book.find(name)    
    return f"{Fore.GREEN}Phone number for {name} is {'; '.join(p.value for p in record['phones'])}{Fore.RESET}"
