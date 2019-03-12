import sql_operations.user_functions as user
from random_data.numbers import*
import sql_operations.acc_functions as acc

class Optional_labels():
    label_name_out = ''
    label_id_out = ''
    label_pl_number_out = None
    label_pl_amount_out = None
    label_eur_number_out = None
    label_eur_amount_out = None


def acc_id_creation(user_id,currency):
    return str(user_id)+'_'+currency


def add_account(user_id,currency):
    holder_name = user.display_data_user(name=user_id)
    user.create_account(user_id=user_id, acc_key=acc_id_creation(user_id=user_id, currency=currency),
                        number=random_acc_number(), currency=currency)

def delete_account(acc_id):
    acc.remove_account(acc_id=acc_id)


def change_name_out(new_name):
    Optional_labels.label_name_out = new_name