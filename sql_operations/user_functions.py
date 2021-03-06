from sql_operations.connection import*
from sql_operations.table_creation import*
import sql_operations.acc_functions as account
from sql_operations.global_variables import*

def add_user(name, table = 'Users',pl_acc_id='NULL', eur_acc_id='NULL', adress='bank_data\\bank.db'):
    con = connector(adress)
    with con:
        cur = con.cursor()
        try:
            Global_var.global_user_id += 1 # GLOBAL USAGE
            parameters = (Global_var.global_user_id, name, pl_acc_id, eur_acc_id)
            cur.execute("INSERT INTO {} VALUES(?,?,?,?)".format(table), parameters)
            con.commit()
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
    return False

# acc_id CREATED IN UPPER FUNCTIONS
def create_account(user_id, acc_id, number, currency, adress='bank_data\\bank.db', user_table='Users'):
    holder = display_data_user(name=user_id)
    account.add_account(acc_id=acc_id, holder=holder, number=number, currency=currency, adress=adress)
    con = connector(adress)
    with con:
        cur = con.cursor()
    command = "UPDATE {} SET {} = \"{}\"  WHERE user_id = {};".format(user_table, currency +'_acc_id', acc_id, user_id)
    cur.execute(command)
    con.commit()

#AGRUMENTS SHOULD BE ENTERED THIS WAY: PL_acc_id= [user id to be checked]
def display_data_user(adress='bank_data\\bank.db', user_table='Users', **arguments):
    con = connector(adress)
    with con:
        cur = con.cursor()
    for key_word, arg in arguments.items():
        cur.execute("SELECT {} FROM {} WHERE user_id = \"{}\"".format(str(key_word),user_table,arg))
        return cur.fetchall()[0][0]


def remove_acc_from_user(user_id,currency,adress='bank_data\\bank.db', user_table='Users'):
    con = connector(adress)
    with con:
        cur = con.cursor()

    if currency == 'PL':
        command = "UPDATE {} SET PL_acc_id = \"NULL\" WHERE user_id = {}".format(user_table,user_id)
        cur.execute(command)
        con.commit()
    elif currency == 'EUR':
        cur.execute("UPDATE {} SET EUR_acc_id = \"NULL\" WHERE user_id = {}".format(user_table,user_id))
        con.commit()


def clear_table(table='Users',adress='bank_data\\bank.db'):
    user_table(name=table)