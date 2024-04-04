from collections import UserDict
from datetime import datetime, timedelta
from classes import RecordFindError


class AddressBook(UserDict):
    def add_record(self, record):
        """
        Create record in adress book.
        
        Parameters:
            record (Record): record in adress book.
        """
        self.data[record.name.value] = record


    def delete(self, name):
        """
        Delete user by name in adress book.
        
        Parameters:
            name: user name in adress book.
        """
        if not name in self.data:
            raise RecordFindError(f"User {name} not found.")        
        self.data.pop(name)


    def find(self, name):
        """
        Find user by name in adress book.
        
        Parameters:
            name: user name in adress book.
        """
        return self.data.get(name)
        
                
    def get_upcoming_birthdays(self):
        """
        Get list of upciming birthdays in a week of users in adress book.
        """
        today = datetime.today().date()

        birthday_congratulate_list = []

        for item in self.data:
            # get user from adress book   
            user = self.data.get(item)
            # get user birthday 
            user_birthday = user['birthday'].value         

            birthday_this_year = user_birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            
            if 0 <= (birthday_this_year - today).days <= 7:               
                if birthday_this_year.weekday() == 5:
                    birthday_this_year = birthday_this_year + timedelta(days=2)
                    
                elif birthday_this_year.weekday() == 6:
                    birthday_this_year = birthday_this_year + timedelta(days=1)

                birthday_date = birthday_this_year.strftime('%Y.%m.%d')
                
                birthday_congratulate_list.append({'name': user['name'].value, 'congratulation_date': birthday_date})
        
        return birthday_congratulate_list