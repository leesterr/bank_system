from bank_database import dataset
from __init__ import time_inserter


class BankFlow:

    def __init__(self):
        self.bank_data = dataset()
        self.time = time_inserter()
        self.pin_store = []
        self.deposit = []



    def acc_create(self):
        print('Bank Account Creation')
        first_name = str(input('Enter your first name >> '))
        last_name = str(input('Enter your last name >> '))
        pin_number = int(input('Set your pin number >> '))
        day_time = self.time
        opening_deposits = int(input('Make your first opening deposits >> '))
        while True:
            confirm_pin = int(input('Confirm your pin number to create an account >> '))
            if confirm_pin == pin_number:
                self.bank_data.data_inserting(first_name, last_name, pin_number, opening_deposits, day_time)
                self.pin_store.append(pin_number)
                print(f'Dear {first_name.capitalize()}, You have successfully created your account on {day_time}. Thank you')
                break
            else:
                print('Try again, you have entered wrong pin number')

    def depositing_income(self, name, pin):
        self.bank_data.cursor_point.execute(f'''SELECT rowid, * FROM customer_details
                                                   WHERE first_name = "{name}" AND pin = {pin}''')
        items = self.bank_data.cursor_point.fetchall()
        if len(items) != 0:
            for item in items:
                print(item[1], item[2])
            depositing = input('Deposit money here >> ')
            self.bank_data.cursor_point.execute(f'''UPDATE customer_details SET deposits = {depositing}
                                                WHERE pin = {pin}''')
            print(f'you have successfully deposited your account with {depositing} amount')
        else:
            print('ERROR!!: Information you have entered does not match to any record!')

    def check_balance(self, name, pin):
        self.bank_data.cursor_point.execute(
            f'SELECT rowid, * FROM customer_details WHERE first_name = "{name}" AND pin = {pin}')
        items = self.bank_data.cursor_point.fetchall()
        if len(items) != 0:
            for item in items:
                print(f'Dear {item[1]} Your balance is: ${item[4]}')

    def commiting_data(self):
        self.bank_data.committing()


f = BankFlow()
f.acc_create()
#f.depositing_income(str(input('Enter your first name >> ')), int(input('Enter your pin >> ')))
#f.check_balance(str(input('Enter your first name >> ')), int(input('Enter your pin >> ')))
f.commiting_data()

