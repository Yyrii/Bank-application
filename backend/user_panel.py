import sql_operations.user_functions as user
from random_data.numbers import*
import sql_operations.acc_functions as acc

class User_labels():
    name = ''
    id = ''
    pl_number = None
    pl_amount = None
    eur_number = None
    eur_amount = None

    def return_var(self, arg):
        options_dic = {
            'name': self.name,
            'id': self.id,
            'pl_number' : self.pl_number,
            'pl_amount' : self.pl_amount,
            'eur_number' : self.eur_number,
            'eur_amount' : self.eur_amount
        }
        return options_dic[arg]

    #def change_var



def acc_id_creation(user_id,currency):
    return str(user_id)+'_'+currency


def add_account(user_id,currency):
    holder_name = user.display_data_user(name=user_id)
    user.create_account(user_id=user_id, acc_key=acc_id_creation(user_id=user_id, currency=currency),
                        number=random_acc_number(), currency=currency)

def delete_account(acc_id):
    acc.remove_account(acc_id=acc_id)


def change_name_out(new_name):
    User_labels.name = new_name