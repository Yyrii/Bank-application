import unittest
import sqlite3 as lite
from sql_operations.user_functions import*
from sql_operations.table_creation import*
from sql_operations.acc_functions import*


#SUPPORTIVE PART
adress = '..\\tests\\database_test.db'
table = 'Users'
table2='Accounts'


#TESTING PART
class Testing_sql_functions(unittest.TestCase):

    def test_checking_user(self):
        add_user(table,123,'Any',adress=adress)
        self.assertTrue(check_for_user(table,name='Any',user_id=123,adress=adress))

    def test_checking_user_f(self):
        self.assertFalse(check_for_user(table,name='Any2',user_id=123,adress=adress))

    def test_checking_acc(self):
        add_account(1324,None,111111,table=table2,adress=adress,amount=2500)
        self.assertTrue(check_for_acc(table2,number=111111,adress=adress))

    def test_checking_acc_f(self):
        self.assertFalse(check_for_acc(table2,number=1111117,adress=adress))

    def test_money_checking(self):
        self.assertEqual(check_money(1324,adress=adress,table=table2),2500)

    def test_display_user(self):
        self.assertEqual(display_data_user(name=123, adress=adress, user_table=table), 'Any')

    def test_display_acc(self):
        self.assertEqual(display_data_acc(holder=1324,adress=adress,acc_table=table2),None)


if __name__ == '__main__':
    user_table(table,adress=adress)
    account_table(table2,adress=adress)
    unittest.main()