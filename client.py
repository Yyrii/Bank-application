import sql_operations.table_creation as create
import sql_operations.acc_functions as acc
import sql_operations.user_functions as user

acc_table = 'Accounts'
user_table = 'Users'


if __name__ == "__main__":
    create.account_table(acc_table)
    acc.add_account(acc_table, 1, 'Andrzej', 123452342, 200, 'PL')
    acc.add_account(acc_table, 2, 'bober', 5555555, 1200, 'EUR')
    acc.remove_account(acc_table, 2)

    create.user_table(user_table)
    user.add_user(user_table,1,'ktos','as12')
