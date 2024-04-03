from collections import UserDict
from datetime import datetime, timedelta
from errors import RecordFindError
from record import Record

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


    def delete(self, name):
        if not name in self.data:
            raise RecordFindError(f"User {name} not found.")        
        self.data.pop(name)


    def find(self, name):
        user = self.data.get(name)
        if user:
            return user
        else:
            raise RecordFindError(f"User {name} not found.") 
        
    def get_upcoming_birthdays(self):
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


book = AddressBook()

    # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
john_record.add_birthday('05.04.1994')

    # Додавання запису John до адресної книги
book.add_record(john_record)

#     # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
jane_record.add_birthday('07.04.1994')
book.add_record(jane_record)

#     # Виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(record)

#     # Знаходження та редагування телефону для John
john = book.find("John")
# john.edit_phone("1234567890", "1112223333")

john = book.get_upcoming_birthdays()

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

#     # Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

#     # Видалення запису Jane
# book.delete("Jane")