import sql_operations.table_creation as create
import sql_operations.acc_functions as acc
import sql_operations.user_functions as user
from interface.App import*

acc_table = 'Accounts'
user_table = 'Users'


if __name__ == "__main__":
    create.account_table(acc_table)
    acc.add_account(acc_table, 1, 'Andrzej', 123452342, 200, 'PL')
    acc.add_account(acc_table, 2, 'bober', 5555555, 1200, 'EUR')
    acc.remove_account(acc_table, 2)

    acc.deposit(acc_table,1,400)

    create.user_table(user_table)
    user.add_user(user_table,1,'ktos')
    user.add_user(user_table,2,'ktos2')
    user.add_user(user_table,3,'ktos2')
    user.add_user(user_table,4,'ktos2')
    user.add_user(user_table,5,'ktos2')

    print(user.check_for_user(name='kto'))
    user.clear_table()

    app = BankApplication()
    app.mainloop()