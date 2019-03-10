import sqlite3 as lite


#konto: id, właściciel, numer konta, hajs, waluta
def account_table(name, adress='bank_data\\bank.db'):
    con = lite.connect(adress)

    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS {}".format(name))
        cur.execute("CREATE TABLE {}(acc_id TEXT PRIMARY KEY ASC, holder TEXT, number INT UNIQUE, amount INT, currency TEXT)".format(name))


# użytkownik: id, nazwa, id połączone z walutowym złotówkowym, z euro
def user_table(name, adress='bank_data\\bank.db'):
    con = lite.connect(adress)

    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS {}".format(name))
        cur.execute("CREATE TABLE {}(user_id INT PRIMARY KEY ASC, name TEXT, PL_acc_id TEXT, EUR_acc_id TEXT)".format(name))