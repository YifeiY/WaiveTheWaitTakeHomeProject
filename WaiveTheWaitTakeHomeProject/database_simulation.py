import sqlite3
import os
import time
DATABASE_FILENAME = 'database.db'



def main():
    connection = initialize_database()
    start_database_simulation(connection=connection)


def initialize_database():
    '''initialize the default database and return the connection'''
    if DATABASE_FILENAME in os.listdir(): os.remove(DATABASE_FILENAME)
    connection = sqlite3.connect(DATABASE_FILENAME)
    cursor = connection.cursor()
    cursor.execute('''create table appointments (id, date, time, person_id, name, status)''')
    cursor.execute('''create table people (person_id, age)''')
    cursor.execute('''insert into appointments VALUES (1, '2021-01-03','10:00',5,'Bob','a')''')
    cursor.execute('''insert into people VALUES (2,20)''')
    cursor.execute('''select * from people ''')
    connection.commit()
    return connection


def start_database_simulation(connection, transaction_filename = 'WaiveTheWaitTakeHomeProject/'
                                                                 'database_transactions'):
    '''execute a preset of transactions specified in teh transaction file'''
    cursor = connection.cursor()
    transactions = open(transaction_filename).readlines()
    for row in transactions:
        print(row)
        if row[:4] == 'wait':
            time.sleep(int(row.split()[1]))
        else:
            cursor.execute(str(row))

    cursor.execute('''select * from appointments''')
    print('appointments final db',cursor.fetchall())

    cursor.execute('''select * from people''')
    print('people final db',cursor.fetchall())

    connection.commit()

if __name__ == "__main__":
    main()