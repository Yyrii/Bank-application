from sql_operations.connection import*


def add_account(table, key, holder, number, amount=1000, currency='PL', adress='bank_data\\bank.db'):
    con = connector(adress)
    parameters = (key, holder, number, amount, currency)
    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO {} VALUES(?,?,?,?,?)".format(table), parameters)

def remove_account(table, key, adress='bank_data\\bank.db'):
    con = connector(adress)
    with con:
        cur = con.cursor()
        cur.execute("DELETE FROM {} WHERE acc_id={}".format(table,key))

def deposit(table, key, money, adress='bank_data\\bank.db'):
    con = connector(adress)
    with con:
        cur = con.cursor()
        cur.execute("UPDATE {} SET amount=amount + {} WHERE acc_id={}".format(table,money,key))