import unittest
import sqlite3 as lite
from sql_operations.user_functions import*
from sql_operations.table_creation import*


#SUPPORTIVE PART
adress = '..\\tests\\database_test.db'
table = 'Users'


#TESTING PART
class Testing_sql_functions(unittest.TestCase):

    def test_checking_user(self):
        add_user(table,123,'Any',adress=adress)
        self.assertTrue(check_for_user(table,name='Any',user_id=123,adress=adress))

    def test_checking_user(self):
        add_user(table,123,'Any',adress=adress)
        self.assertFalse(check_for_user(table,name='Any2',user_id=123,adress=adress))

if __name__ == '__main__':
    user_table(table,adress=adress)
    unittest.main()