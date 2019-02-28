import sqlite3



# utworzenie połączenia z bazą przechowywaną na dysku
connection = sqlite3.connect('bank_data\\bank.db')

# dostęp do kolumn przez indeksy i przez nazwy
connection.row_factory = sqlite3.Row

# utworzenie obiektu kursora
cur = connection.cursor()

# tworzenie tabel
cur.execute("DROP TABLE IF EXISTS list_of_accounts;")

cur.execute("""
    CREATE TABLE IF NOT EXISTS list_of_accounts (
        id INTIGER PRIMARY KEY ASC,
        holder_name varchar(25) NOT NULL,
        account_number int DEFAULT '',
        amount int DEFAULT 0
    )""")



# wstawiamy jeden rekord danych
cur.execute('INSERT INTO list_of_accounts VALUES({}, ?, ?,?);'.format(135), ('karol', '123456789','100'))
cur.execute('INSERT INTO list_of_accounts VALUES({}, ?, ?,?);'.format(445), ('pioter', '222456789','5000'))

connection.commit()


######################################################