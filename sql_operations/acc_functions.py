from sql_operations.connection import*
from sql_operations.table_creation import*


def add_account(acc_id, holder, number, amount=0, table='Accounts', currency='PL', adress='bank_data\\bank.db'):
    con = connector(adress)
    parameters = (acc_id, holder, number, amount, currency)
    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO {} VALUES(?,?,?,?,?)".format(table), parameters)

def remove_account(acc_id, table='Accounts', adress='bank_data\\bank.db'):
    con = connector(adress)
    with con:
        cur = con.cursor()
        command = "DELETE FROM {} WHERE acc_id=\"{}\"".format(table, str(acc_id))
        cur.execute(command)

def deposit(acc_id, money, table='Accounts', adress='bank_data\\bank.db'):
    con = connector(adress)
    with con:
        cur = con.cursor()
        cur.execute("UPDATE {} SET amount=amount + {} WHERE acc_id={}".format(table, money, acc_id))

def clear_table(table='Accounts',adress='bank_data\\bank.db'):
    account_table(name=table)


def check_for_acc(table='Accounts', adress='bank_data\\bank.db',**arguments):
    con = connector(adress)
    with con:
        cur = con.cursor()
    for key_word, arg in arguments.items():
        cur.execute("SELECT {} FROM {} WHERE {} = \"{}\"".format(key_word,table,key_word,arg))
        results = cur.fetchall()
        if len(results) > 0:
            return True
        else:
            return False


def check_money(acc_id, table='Accounts', adress='bank_data\\bank.db'):
    con = connector(adress)
    with con:
        cur = con.cursor()
        cur.execute("SELECT amount FROM {} WHERE acc_id = \"{}\"".format(table,acc_id))
        return cur.fetchall()[0][0]


#AGRUMENTS SHOULD BE ENTERED THIS WAY: holder= [acc id to be checked]
def display_data_acc(adress='bank_data\\bank.db', acc_table='Accounts',**arguments):
    con = connector(adress)
    with con:
        cur = con.cursor()
    for key_word, arg in arguments.items():
        cur.execute("SELECT {} FROM {} WHERE acc_id = \"{}\"".format(key_word,acc_table,arg))
        return cur.fetchall()[0][0]
