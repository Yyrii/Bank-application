import sqlite3 as lite


def connector(adress):
    return lite.connect(adress)
