import sql_operations.table_creation as create
import sql_operations.acc_functions as fun

acc_table = 'Accounts'
user_table = 'Users'


if __name__ == "__main__":
    create.account_table(acc_table)
    fun.add_account(1,'Andrzej',123452342,200,'PL')
    fun.add_account(2, 'bober', 5555555, 1200,'EUR')
    fun.remove_account(acc_table, 2)

    create.user_table(user_table)

