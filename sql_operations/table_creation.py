import sqlite3 as lite


def table():
    con = lite.connect('bank_data\\bank.db')

    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Accounts")
        cur.execute("CREATE TABLE Accounts(Id INT PRIMARY KEY ASC, holder TEXT, number INT, amount INT)")