from codextract_bank.bank_database import DataSet, IdGenerator
from codextract_bank import banner
import sys

customer = DataSet()
id_number = IdGenerator()
print(banner)
while True:
    print('''Select an option by entering its serial number
    1-Creating new bank account 
    2-Banking activities 
    type any number to terminate the program
    ''')
    option = input('>> ')
    returning_pin = ''
    if int(option) == 1:
        first_name = str(input('First name: '))
        last_name = str(input('Last name: '))
        pin_number = id_number.generator()
        print(f'\nYou pin ID is:  {pin_number}  Type \'exit\' to terminate the program')
        count = 0
        while count < 3:
            inserter = str(input('Enter pin you have received to continue creating account: '))
            if inserter == pin_number:
                customer.customer_details_inserting(first_name, last_name, pin_number)
                id_pin = customer.getting_pin(first_name, last_name)
                returning_pin += id_pin
                customer.customer_value_inserting(pin_number)
                print(f'Dear {first_name.capitalize()}, you have successfully created your account')
                print('please keep your pin ID private')
                print('\nMake your first deposits!!')
                while True:
                    request = str(input('Enter your id: '))
                    if request == id_pin:
                        if customer.id_number(request):
                            print(customer.id_number(request))
                            customer.income_deposits(request, int(input('First deposit money of amount: ')))
                            customer.committing()
                            print('Congratulations! Enjoy CodeXtract bak services. Terms and conditions apply.')
                            print(banner)
                            break
                    elif request == 'exit':
                        print(banner)
                        sys.exit('You have successfully terminated the process')
                    else:
                        print(f'No details found with {request}')
                break
            elif inserter == 'exit':
                print(banner)
                sys.exit('You have successfully cancelled the process')
            else:
                print('Non identical pin Id')
            count += 1
            if count > 3:
                print('Enter details again')

    elif int(option) == 2:
        while True:
            print('\nBanking activities!')
            print('''Select an option by indicating the serial number
                   1-Check balance
                   2-Deposit income
                   3-Withdraw money''')
            bank_option = int(input('>>> '))
            if bank_option == 1:
                request = str(input('Enter your id: '))
                if customer.id_number(request):
                    print(customer.id_number(request))
                    customer.getting_customer_balances(request)
                elif request == 'exit':
                    sys.exit('You have successfully terminated the process')
                else:
                    print(f'No details found with "{request}" Pin ID')

            elif bank_option == 2:
                request = str(input('Enter your id: '))
                if customer.id_number(request):
                    print(customer.id_number(request))
                    new = customer.withdrawal_pulling(request)
                    figure, *other = new
                    amount = input('Enter amount to deposit: ')
                    new_amount = int(figure) + int(amount)
                    customer.income_deposits(request, new_amount)
                    customer.committing_time_modify(request, customer.date_detail)
                    customer.committing()
                    print(
                        f'You have successfully deposited money amount: ${int(amount):,}, your new balance is: '
                        f'${new_amount:,}')
                elif request == 'exit':
                    print(banner)
                    sys.exit('You have successfully terminated the process')
                else:
                    print('Wrong pin')

            elif bank_option == 3:
                request = str(input('Enter your id: '))
                if customer.id_number(request):
                    print(customer.id_number(request))
                    new = customer.withdrawal_pulling(request)
                    figure, *other = new
                    amount = input('Enter amount to withdraw: ')
                    if int(figure) >= int(amount):
                        new_amount = int(figure) - int(amount)
                        customer.income_deposits(request, new_amount)
                        customer.committing_time_modify(request, customer.date_detail)
                        customer.committing()
                        print(f'You have successfully withdrawn: ${int(amount):,}, Your remaining balance is: '
                              f'${new_amount:,}')
                    else:
                        print('Insufficient balances')
                else:
                    print('wrong pin\n')
            else:
                print(banner)
                sys.exit('You have successfully terminated the process')
    else:
        print('You have successfully terminated the process')
        break
