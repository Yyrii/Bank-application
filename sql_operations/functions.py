import sqlite3 as lite

adress = 'bank_data\\bank.db'
table_name = 'Accounts'

def connector(adress):
    return lite.connect(adress)


def add_account(key, holder, number, starting_amount=1000):
    con = connector(adress)
    parameters = (key,holder,number,starting_amount)
    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO Accounts VALUES(?,?,?,?)", parameters)


def table():
    con = connector(adress)

    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO Accounts VALUES(1,'Michelle', 123456789,1000)")
        cur.execute("INSERT INTO Accounts VALUES(2,'andrzej', 999999999, 1000)")