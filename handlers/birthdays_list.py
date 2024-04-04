from colorama import Fore
from handlers.input_error import input_error


@input_error
def birthdays_list(book):
    """
    Return birthdays list during next week for contacts in adress book.
        
    Parameters:
        book (AdressBook): adress book instance.
    """
    birthday_list = []
    
    birthdays_a_week = book.get_upcoming_birthdays()

    for birthday in birthdays_a_week:
        birthday_list.append(f"{Fore.GREEN}{birthday['name']}, congratulate on: {birthday['congratulation_date']}{Fore.RESET}")

    if birthday_list:
        return '\n'.join(birthday_list)
    else:
        return f"{Fore.GREEN}There are no birthdays this week.{Fore.RESET}"
    
