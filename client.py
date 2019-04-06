import sql_operations.table_creation as create
import sql_operations.acc_functions as acc
import sql_operations.user_functions as user
from interface.App import*
import backend.front_panel as b_end
from face_recognition.face_images import remove_images

acc_table = 'Accounts'
user_table = 'Users'


if __name__ == "__main__":
    create.account_table(acc_table)
    create.user_table(user_table)
    remove_images()


    app = BankApplication()
    app.mainloop()