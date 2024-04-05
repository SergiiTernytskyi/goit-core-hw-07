from datetime import datetime
from classes import Field
from classes import BirthdayError


class Birthday(Field):
    def __init__(self, value):
        try:
            birthday = datetime.strptime(value, '%d.%m.%Y')                    
        except ValueError:
            raise BirthdayError("Invalid date format. Use birthday date in format DD.MM.YYYY.")
        
        if birthday >= datetime.today():
            raise BirthdayError(f'Birthday date cannot be in a future.')
        
        self.value = birthday.date()
    
    def __str__(self):
        return f"{self.value.strftime('%Y.%m.%d')}"