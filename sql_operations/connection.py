import sqlite3 as lite

adress = 'bank_data\\bank.db'

def connector(adress):
    return lite.connect(adress)
