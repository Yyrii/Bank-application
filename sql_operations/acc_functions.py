import sqlite3 as lite

adress = 'bank_data\\bank.db'
table_name = 'Accounts'

def connector(adress):
    return lite.connect(adress)


def add_account(key, holder, number, starting_amount=1000, currency='PL'):
    con = connector(adress)
    parameters = (key,holder,number,starting_amount,currency)
    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO Accounts VALUES(?,?,?,?,?)", parameters)

def remove_account(table, key):
    con = connector(adress)
    with con:
        cur = con.cursor()
        cur.execute("DELETE FROM {} WHERE acc_id={}".format(table,key))
