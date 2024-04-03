from field import Field
from errors import PhoneVerificationError

class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise PhoneVerificationError("Phone number is less than 10 symbols")
            
