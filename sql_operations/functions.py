import sqlite3 as lite


def table():
    con = lite.connect('bank_data\\bank.db')

    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO Accounts VALUES(1,'Michelle', 123456789,1000)")
        cur.execute("INSERT INTO Accounts VALUES(2,'andrzej', 999999999, 1000)")