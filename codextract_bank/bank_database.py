import sqlite3
import random
from codextract_bank import banner
import string
from codextract_bank import time_inserter as tp


class DataSet:

    # Initializing a connection to database and a cursor

    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.cursor_point = self.connection.cursor()
        self.date_detail = tp()

    def printing_tables(self):
        self.cursor_point.execute('SELECT * FROM sqlite_schema WHERE type = "table"')
        items = self.cursor_point.fetchall()
        if len(items) != 0:
            for item in items:
                print(item)
        else:
            print('No tables found')

    # Creating a customers name table
    def table(self):
        self.cursor_point.execute('''CREATE TABLE IF NOT EXISTS customer_details(
                                  first_name TEXT,
                                  last_name TEXT,
                                  id_number TEXT,
                                  time TEXT,
                                  FOREIGN KEY(id_number) REFERENCES customer_values(pin_id))''')

    # Creating customer values table
    def values_table(self):
        self.cursor_point.execute('''CREATE TABLE IF NOT EXISTS customer_values(
        pin_id TEXT,
        committing_time TEXT,
        balances INTEGER)''')

    def table_drop(self):
        self.cursor_point.execute('DROP TABLE customer_details')
        self.cursor_point.execute('DROP TABLE customer_values')
        print('Tables dropped successfully')

    # Inserting data into customer_details table
    def customer_details_inserting(self, firstname='', lastname='', customer_id=''):
        self.cursor_point.execute(f'''INSERT INTO customer_details VALUES
         ("{firstname}","{lastname}", "{customer_id}", "{self.date_detail}")''')

    # Inserting data into customer_values table
    def customer_value_inserting(self, customer_pin=''):
        self.cursor_point.execute(f'INSERT INTO customer_values VALUES ("{customer_pin}", "{self.date_detail}", {0})')

    # Getting customers pin by names
    def getting_pin(self, firstname, lastname):
        self.cursor_point.execute(f'''SELECT id_number FROM customer_details WHERE
         first_name = "{firstname}" AND last_name = "{lastname}"''')
        items = self.cursor_point.fetchone()
        for item in items:
            return item

    # A function to update balances after withdrawing or depositing
    def income_deposits(self, customer_pin, deposits):
        self.cursor_point.execute(f'UPDATE customer_values SET balances = {deposits} WHERE pin_id = "{customer_pin}"')

    # A function to modify committing time in the details table after deposit or withdraw
    def committing_time_modify(self, customer_pin, committing_time):
        self.cursor_point.execute(f'''UPDATE customer_values SET committing_time = "{committing_time}"
         WHERE pin_id = "{customer_pin}"''')

    # A function to show balances using pin_id, ready to modify
    def withdrawal_pulling(self, customer_pin):
        self.cursor_point.execute(f'SELECT balances FROM customer_values WHERE pin_id = "{customer_pin}"')
        items = self.cursor_point.fetchone()

        def i(m):
            return m
        item = list(map(i, items))
        return item

    # Connecting all tables
    def connecting_tables(self):
        self.cursor_point.execute(f'''SELECT * FROM customer_details
                                   INNER JOIN customer_values ON customer_details.id_number = customer_values.pin_id''')
        items = self.cursor_point.fetchall()
        for item in items:
            print(item)

    def getting_customer_balances(self, pin):
        self.cursor_point.execute(f'''SELECT balances FROM customer_values WHERE pin_id = "{pin}"''')
        items = self.cursor_point.fetchall()
        if len(items) != 0:
            def details(s):
                self.cursor_point.execute(f'''SELECT first_name, last_name FROM customer_details WHERE
                 id_number = "{s}"''')
                new_items = self.cursor_point.fetchall()
                for first, last in new_items:
                    return f'Dear {first.capitalize()} {last.capitalize()}'
            item = list(map(lambda x: x, items))
            balance, *others = item
            for balances in balance:
                print(f'{details(pin)} You have ${balances:,} in your account')
        else:
            print('Wrong pin id')

    # Making queries and fetching data
    def fetching(self):
        self.cursor_point.execute('SELECT rowid, * FROM customer_details')
        items = self.cursor_point.fetchall()
        if len(items) != 0:
            for item in items:
                print(item)
        else:
            print('The table is empty')

    # Finding a row by specific id number
    def id_number(self, customer_pin):
        self.cursor_point.execute(f'''SELECT first_name, last_name FROM customer_details
         WHERE id_number = "{customer_pin}"''')
        items = self.cursor_point.fetchall()
        if len(items) != 0:
            for first, last in items:
                return f'Welcome {first.capitalize()} {last.capitalize()}'

    # Finding a row by name-like
    def name_like(self, firstname):
        self.cursor_point.execute(f'SELECT rowid, * FROM customer_details WHERE first_name LIKE "{firstname}%"')
        items = self.cursor_point.fetchall()
        if len(items) != 0:
            for item in items:
                print(item)
        else:
            print('No data found')

    # Finding a row by first name
    def name_similar(self, firstname):
        self.cursor_point.execute(f'SELECT rowid, * FROM customer_details WHERE first_name = "{firstname}"')
        items = self.cursor_point.fetchall()
        if len(items) != 0:
            for item in items:
                print(item)
        else:
            print('No data found')

    # Finding a row by first name or id
    def name_or_id(self, firstname, identity):
        self.cursor_point.execute(f'''SELECT rowid, * FROM customer_details WHERE
         first_name = "{firstname}" OR rowid = "{identity}"''')
        items = self.cursor_point.fetchall()
        if len(items) != 0:
            for item in items:
                print(item)
        else:
            print('No data found')

    # Update an existing data
    def updating_name_via_id(self, firstname, identity):
        self.cursor_point.execute(f'UPDATE customer_details SET first_name = "{firstname}" WHERE rowid = "{identity}"')

    # Deleting the user
    def getting_deleted_customer(self, customer_id) -> str:
        self.cursor_point.execute(f'''SELECT balances FROM customer_values WHERE pin_id = "{customer_id}"''')
        items = self.cursor_point.fetchall()
        if len(items) != 0:
            def details(s):
                self.cursor_point.execute(f'''SELECT first_name, last_name FROM customer_details WHERE
                         id_number = "{s}"''')
                new_items = self.cursor_point.fetchall()
                for first, last in new_items:
                    return f'{first.capitalize()} {last.capitalize()}'
            item = list(map(lambda x: x, items))
            balance, *others = item
            data = [details(customer_id)]
            for balances in balance:
                data.append(f'{balances}')
            return ' '.join(list(map(lambda x: x, data)))

    def deleting_customer(self, customer_id):
        self.cursor_point.execute(f'DELETE FROM customer_values WHERE pin_id IN '
                                  f'(SELECT id_number FROM customer_details WHERE pin_id = "{customer_id}")')

    # Committing an update after a query
    def committing(self):
        self.connection.commit()

    # CLosing the database after some transactions
    def closing_db(self):
        self.connection.close()


class IdGenerator:

    @staticmethod
    def generator():
        container = list(string.ascii_uppercase + string.digits + string.ascii_lowercase + '_-')
        random.shuffle(container)
        pin_number = ''
        for n in range(13):
            pin_number += str(container[n])
        return pin_number


if __name__ == '__main__':
    print(banner)
