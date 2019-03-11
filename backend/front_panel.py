import sql_operations.user_functions as user
import sql_operations.acc_functions as acc
from random_data.id_name import*
from random_data.numbers import*
from sql_operations.global_variables import*
import backend.user_panel as user_panel


user_table = 'Users'
def register(input_name,adress='bank_data\\bank.db'):
    user.add_user(user_table,input_name,adress=adress)
    Global_var.current_user_id = Global_var.global_user_id
    user_panel.Optional_labels.label_name_out = Global_var.current_user_id
    return Global_var.current_user_id


def login(input_id,adress='bank_data\\bank.db'):
    if user.check_for_user(user_id=input_id,adress=adress) == True:
        Global_var.current_user_id = input_id
        user_panel.Optional_labels.label_name_out = Global_var.current_user_id
        return Global_var.current_user_id
