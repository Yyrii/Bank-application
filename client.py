import sql_operations.table_creation as create
import sql_operations.acc_functions as acc
import sql_operations.user_functions as user
from interface.App import*

acc_table = 'Accounts'
user_table = 'Users'


if __name__ == "__main__":
    create.account_table(acc_table)
    acc.add_account(1, None, 123452342, 200, currency='PL',table=acc_table)
    acc.add_account(2, None, 5555555, 1200, currency='EUR',table=acc_table)
    acc.remove_account(2,table=acc_table)

    acc.deposit(1,400,table=acc_table)

    create.user_table(user_table)
    user.add_user(user_table,'ktos')
    user.add_user(user_table,'ktos2')
    user.add_user(user_table,'ktos2')
    user.add_user(user_table,'ktos2')
    user.add_user(user_table,'ktos2')

    #print(user.check_for_user(name='kto'))

    user.create_account(2,'user2_pl',41241414,'PL')
    print(acc.check_money(1))

    app = BankApplication()
    app.mainloop()