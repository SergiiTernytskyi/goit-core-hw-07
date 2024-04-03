import re
from field import Field
from errors import PhoneVerificationError

class Phone(Field):
    def __init__(self, value):
        if not re.fullmatch(r'(\+?38)?\d{10}', value):
            raise PhoneVerificationError(f'Wrong phone number format: {value}')
        
        super().__init__(value)

            
