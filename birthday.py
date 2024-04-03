from datetime import datetime
from field import Field
from errors import BirthdayError


class Birthday(Field):
    def __init__(self, value):
        try:
            birthday = datetime.strptime(value, '%d.%m.%Y')                    
        except ValueError:
            raise BirthdayError("Invalid date format. Use birthday date in format DD.MM.YYYY.")
        
        if birthday >= datetime.today():
            raise BirthdayError(f'Birthday date cannot be in a future.')
        
        self.value = birthday.date()