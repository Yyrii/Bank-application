import sql_operations.table_creation as create
import sql_operations.functions as fun

#table_name = 'Accounts'

if __name__ == "__main__":
    create.table()
    fun.add_account(1,'Andrzej',123452342,200)
    fun.add_account(2, 'bober', 5555555, 1200)

