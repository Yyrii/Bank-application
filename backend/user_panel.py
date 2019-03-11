import sql_operations.user_functions as user
from random_data.numbers import*

class Optional_labels():
    label_name_out = ''
    label_id_out = ''
    label_pl_number_out = ''
    label_pl_amount_out = ''
    label_eur_number_out = ''
    label_eur_amount_out = ''


def acc_id_creation(user_id,currency):
    return str(user_id)+'_'+currency


def add_account(user_id,currency):
    user.create_account(holder_name=user_id, acc_key=acc_id_creation(user_id=user_id, currency=currency), number=random_acc_number(), currency=currency)