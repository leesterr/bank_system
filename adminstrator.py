from codextract_bank.bank_database import DataSet

administrator = DataSet()

while True:
    print('''Select an option by entering its serial number
    1-Dropping tables 
    2-Creating tables 
    3-Fetching all values 
    4-Search by ID number 
    5-Search by like character 
    6-Search by exact name 
    7-Search by name or ID 
    8-Updating name via ID 
    9-Printing all tables 
    10-Deleting user details
          ''')
    
    option = int(input('>> '))
    if option == 1:
        administrator.table_drop()

    elif option == 2:
        administrator.table()
        administrator.values_table()

    elif option == 3:
        administrator.connecting_tables()
        break
    elif option == 4:
        administrator.id_number(int(input('Search by id number: ')))
        break

    elif option == 5:
        administrator.name_like(str(input('Search by a like character: ')))
        break

    elif option == 6:
        administrator.name_similar(str(input('Search by exact name: ')))
        break

    elif option == 7:
        administrator.name_or_id(str(input('search by first name or id number, Name: ')), int(input('Id number: ')))
        break

    elif option == 8:
        administrator.updating_name_via_id(str(input('Enter new name: ')), int(input('Enter the updated ID: ')))
        administrator.committing()
        administrator.closing_db()
        break

    elif option == 9:
        administrator.printing_tables()

    elif option == 10:
        print('''1. Confirm\n2. Delete''')
        while True:
            option = input('Chose an option')
            if int(option) == 1:
                customer_id = input('Please enter customer\'s ID number: ')
                details = administrator.getting_deleted_customer(customer_id=str(customer_id))
                if details:
                    first_name, last_name, amount, *other = list(details.split())
                    if int(amount) < 1:
                        print(f'Ready to delete "{first_name, last_name}" account')
                    else:
                        print(f'Cannot delete the account of {first_name} because it has ${int(amount):,} balance.')
                        break
                else:
                    print('No details found with that pin id')
                    break
            elif int(option) == 2:
                administrator.deleting_customer(str(input('Enter customer ID: ')))
                administrator.committing()
                break
        break
    elif option == 11:
        administrator.deleting_customer(customer_id=input('Enter customer id'))
