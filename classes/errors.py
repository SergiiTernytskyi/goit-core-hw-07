class PhoneVerificationError(Exception):
    def __init__(self, message="Phone number does not match the requirements"):
        self.message = message
        super().__init__(self.message)

class PhoneFindError(Exception):
    def __init__(self, message="Phone number does not exists"):
        self.message = message
        super().__init__(self.message)

class RecordFindError(Exception):
    def __init__(self, message="Record does not exists"):
        self.message = message
        super().__init__(self.message)

class BirthdayError(Exception):
    def __init__(self, message="Invalid date format"):
        self.message = message
        super().__init__(self.message)
