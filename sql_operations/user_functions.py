from sql_operations.connection import*


def add_user(table, user_id, name, pl_acc_id='NULL', eur_acc_id='NULL'):
    con = connector(adress)
    parameters = (user_id, name, pl_acc_id, eur_acc_id)
    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO {} VALUES(?,?,?,?)".format(table), parameters)

def remove_user(table, key):
    con = connector(adress)
    with con:
        cur = con.cursor()
        cur.execute("DELETE FROM {} WHERE user_id={}".format(table,key))