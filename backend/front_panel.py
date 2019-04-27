import sql_operations.user_functions as user
import sql_operations.acc_functions as acc
from random_data.random_name import*
from random_data.numbers import*
from sql_operations.global_variables import*
import backend.user_panel as user_panel
from interface.Pages import*


user_table = 'Users'
def register(input_name,adress='bank_data\\bank.db'):
    user.add_user(input_name,table=user_table,adress=adress)
    Global_var.current_user_id = Global_var.global_user_id                        # current = global
    return Global_var().return_current_id()


def login(input_id,adress='bank_data\\bank.db'):
    if user.check_for_user(user_id=input_id,adress=adress) == True:
        Global_var.current_user_id = input_id                                            # setting current user
        return Global_var().return_current_id()

def money_to_everyone():
    acc.add_everyone_money()

def add_n_users(pl_acc = False, eur_acc = False):
    for i in range(10):
        user.add_user(random_name())
        if pl_acc:
            user.create_account(Global_var().return_global_id(),
                                acc_id=(str(Global_var().return_global_id())+'_'+'PL'),number=random_acc_number(),currency='PL')
        if eur_acc:
            user.create_account(Global_var().return_global_id(),
                                acc_id=(str(Global_var().return_global_id()) + '_' + 'EUR'), number=random_acc_number(), currency='EUR')