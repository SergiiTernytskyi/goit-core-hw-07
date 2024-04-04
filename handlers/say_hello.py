from colorama import Fore


def say_hello(name):       
    if(name):
        return (f"{Fore.GREEN}Hello, {name}{Fore.RESET}")
    else:
        return (f"{Fore.GREEN}Hello, Incognito user{Fore.RESET}")
