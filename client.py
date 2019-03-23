import sql_operations.table_creation as create
import sql_operations.acc_functions as acc
import sql_operations.user_functions as user
from interface.App import*
import backend.front_panel as b_end

acc_table = 'Accounts'
user_table = 'Users'


if __name__ == "__main__":
    create.account_table(acc_table)
    acc.add_account(1, None, 123452342, 200, currency='PL',table=acc_table)
    acc.add_account(2, None, 5555555, 1200, currency='EUR',table=acc_table)
    acc.remove_account(2,table=acc_table)

    acc.deposit(1,400,table=acc_table)

    create.user_table(user_table)
    user.add_user('ktos',table=user_table)
    user.add_user('kto23s',table=user_table)
    user.add_user('kt423ros',table=user_table)
    user.add_user('kto23rs',table=user_table)


    #print(user.check_for_user(name='kto'))

    #user.create_account(2,'user2_PL',41241414,'PL')
    #print(acc.check_money(1))

    b_end.register('Karoline')
    b_end.register('Karoline')

    import backend.user_panel as up

    print(up.User_labels().return_var('id'))



    #user_panel.add_account(6,'EUR')
    user_panel.add_account(1, 'PL')
    user_panel.add_account(2, 'PL')
    user_panel.add_account(3, 'PL')
    #user_panel.delete_account('6_EUR')

    acc.add_everyone_money()

    #user_panel.dig_accounts(6)
    #print(user_panel.User_labels().return_var('pl_number'))
    #print(user_panel.User_labels().return_var('eur_number'))

    #print(acc.user_id_by_acc(123452342))

    app = BankApplication()
    app.mainloop()