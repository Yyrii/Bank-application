from sql_operations.connection import*
from sql_operations.table_creation import*

def add_user(table, user_id, name, pl_acc_id='NULL', eur_acc_id='NULL', adress='bank_data\\bank.db'):
    con = connector(adress)
    parameters = (user_id, name, pl_acc_id, eur_acc_id)
    with con:
        cur = con.cursor()
        #if check_for_user(table,name=name,user_id=user_id) == False:
        try:
            cur.execute("INSERT INTO {} VALUES(?,?,?,?)".format(table), parameters)
        except Exception as e:
            print(e)

def remove_user(table, key, adress='bank_data\\bank.db'):
    con = connector(adress)
    with con:
        cur = con.cursor()
        cur.execute("DELETE FROM {} WHERE user_id={}".format(table,key))

#LOOKING FOR EXACT USER DATA, "number" will not be found by "num"
def check_for_user(table='Users', adress='bank_data\\bank.db',**arguments):
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

def clear_table(table='Users',adress='bank_data\\bank.db'):
    user_table(name=table)