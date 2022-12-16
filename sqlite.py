import sqlite3


def createDB():
    conn = sqlite3.connect('staff_registration.db')
    print(' created successfully')
    conn.close()


# createDB()


def createTableDB():
    conn = sqlite3.connect('gold_concept.db')
    print(' database open successfully')

    conn.execute('''CREATE TABLE gold_concept
            (ID INT PRIMARY KEY     NOT NULL,
            QUESTION           TEXT    NOT NULL,
            OPTION1            TEXT    NOT NULL,
            OPTION2            TEXT    NOT NULL,
            OPTION3            TEXT    NOT NULL,
            OPTION4            TEXT    NOT NULL,
            ANSWER            TEXT     NOT NULL);''')

    print('table created successfully')


# createTableDB()

def insert():
    conn = sqlite3.connect('gold_concept.db')
    print(' database open successfully')

    idnumber = input('put your id number here: ')
    question = input('Your Username: ')
    option1 = input('Your option1: ')
    option2 = input('Your option2: ')
    option3 = input('Your option3: ')
    option4 = input('Your option4: ')
    answer = input('do you want to choose he/she as admin. YES or NO : ')

    insert_data = "INSERT INTO gold_concept (ID, QUESTION, OPTION1, OPTION2, OPTION3, OPTION4, ANSWER ) VALUES('"+idnumber+"', '"+question+"', '" + option1 + "', '" + option2 + "', '" + option3 + "', '" + option4 + "', '" + answer + "') "
    conn.execute(insert_data)
    conn.commit()
    print('Record created successfully')
    conn.close()


insert()


def getResult():

    conn = sqlite3.connect('gold_concept.db')
    print(' database open successfully')
    # confirmed = input('Search: ')
    cursor = conn.execute("SELECT id, question, option1, option2, option3, option4 FROM gold_concept")
    for row in cursor:
        # if confirmed == row[3]:

        print(f'Id = {row[0]}')
        print(f'question = {row[1]}')
        print(f'poption1 = {row[2]}')
        print(f'poption2 = {row[3]}')
        print(f'poption3 = {row[4]}')
        print(f'poption4 = {row[5]}')
        # print(f' = {row[3]} ')
        print('====================')

        # elif confirmed == row[3]:

        #     print(f'Id = {row[0]}')
        #     print(f'Name = {row[1]}')
        #     print(f'Password = {row[2]}')
        #     print(f'Admin = {row[3]} ')

        # else:
        #     pass

    print('operation done successfully')
    conn.close()


# getResult()

