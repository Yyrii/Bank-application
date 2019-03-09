import sqlite3 as lite


def connector(adress):
    return lite.connect(adress)

def cursor(adress):
    return lite.connect(adress).cursor()