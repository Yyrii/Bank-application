import sql_operations.user_functions as user
from random_data.numbers import*
import sql_operations.acc_functions as acc
from sql_operations.global_variables import*

class User_labels():
    name = ''
    id = ''
    pl_number = None
    pl_amount = None
    eur_number = None
    eur_amount = None

    def return_var(self, arg):
        self.options_dic = {
            'name': self.name,
            'id': self.id,
            'pl_number' : self.pl_number,
            'pl_amount' : self.pl_amount,
            'eur_number' : self.eur_number,
            'eur_amount' : self.eur_amount
        }

        return self.options_dic[arg]



def acc_id_creation(user_id,currency):
    return str(user_id)+'_'+currency


def add_account(user_id,currency):
    holder_name = user.display_data_user(name=user_id)
    user.create_account(user_id=user_id, acc_key=acc_id_creation(user_id=user_id, currency=currency),
                        number=random_acc_number(), currency=currency)
    #dig_accounts(user_id)

def delete_account(acc_id,user_id):
    acc.remove_account(acc_id=acc_id)
    dig_currency=acc_id.split('_')
    user.remove_acc_from_user(user_id,str(dig_currency[1]))
    #Todo: usunąć połaćzenie z kontem w bazie danych

def dig_accounts(user_id):
    pl_acc_id = user.display_data_user(Pl_acc_id=user_id)
    try:
        User_labels.pl_number = acc.display_data_acc(number=pl_acc_id)
    except:
        #print('user: ',user_id,' has no pl acc')
        User_labels.pl_number = None
        User_labels.pl_amount = None
    eur_acc_id = user.display_data_user(EUR_acc_id=user_id)
    try:
        User_labels.eur_number = acc.display_data_acc(number=eur_acc_id)
    except:
        #print('user: ',user_id,' has no eur acc')
        User_labels.eur_number = None
        User_labels.eur_amount = None

    User_labels.id = Global_var().return_current_id()
    User_labels.name = user.display_data_user(name=Global_var().return_current_id())