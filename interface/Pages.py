import tkinter as tk
import tkinter.ttk as ttk
import sql_operations.user_functions as user_f
from sql_operations.global_variables import*
import backend.user_panel as user_panel
import backend.front_panel as front_panel
import interface.popup as popup
import face_recognition.face_images as f_images
import face_recognition.faces_train as f_train
import face_recognition.identificator as identification
import os

LARGE_FONT = ("Verdana", 12)

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="Bank system", font=LARGE_FONT)
        self.label.pack(pady=10, padx=10)
        controller.geometry("508x292+492+193")


        #SHOW STATS BUTTON
        self.Show_stats = tk.Button(self, text="Show stats",
            command=lambda: None)#[controller.show_frame(UserPanel),printer(self.user_name.get())])#controller.geometry("808x292+492+193"))#printer(user_name.get()))
        self.Show_stats.configure(background="#d9d9d8")
        self.Show_stats.place(relx=0.079, rely=0.685, height=54, width=97)

        #USER NAME INPUT
        self.user_name = tk.StringVar()
        self.Name_input = tk.Entry(self,textvariable=self.user_name)
        self.Name_input.place(relx=0.079, rely=0.271, height=20, relwidth=0.382)

        #TEXT ABOVE INPUT
        self.Name = ttk.Label(self)
        self.Name.place(relx=0.079, rely=0.168, height=19, width=116)
        self.Name.configure(text='Name / id')

        #LOGIN BUTTON
        self.Log_in_b = tk.Button(self,text='Log in',
            command=lambda: self.login(controller))
        self.Log_in_b.place(relx=0.079, rely=0.382, height=54, width=97)
        self.Log_in_b.configure(background="#d9d9d8")

        #REGISTER BUTTON
        self.Register_b = tk.Button(self,text='Register',command=lambda: self.register(controller))
        self.Register_b.place(relx=0.315, rely=0.382, height=54, width=97)
        self.Register_b.configure(background="#d9d9d8")

        # ADD MONEY EVERYWHERE
        self.Add_money = tk.Button(self, text="500+",
                                    command=lambda: self.add_everyone())
        self.Add_money.configure(background="#d9d9d8")
        self.Add_money.place(relx=0.315, rely=0.685, height=54, width=97)

        # ADD USERS
        self.Add_users = tk.Button(self, text="Add 10 users",command=lambda: self.add_n_users())
        self.Add_users.configure(background="#d9d9d8")
        self.Add_users.place(relx=0.555, rely=0.685, height=54, width=97)

        # CURRENCIES
        self.var_pl = 'pl'
        self.Pl_acc_too = tk.Checkbutton(self,text='with PL acc',variable=self.var_pl)
        self.Pl_acc_too.place(relx=0.748, rely=0.700, height=14, width=97)

        self.var_eur = 'eur'
        self.EUR_acc_too = tk.Checkbutton(self, text='with EUR acc', variable=self.var_eur)
        self.EUR_acc_too.place(relx=0.755, rely=0.790, height=14, width=97)

        #REGISTER WITH FACE RECOGNITION
        self.Facial_register = tk.Button(self, text='Register via face',command=lambda: self.register(controller,with_face=True))
        self.Facial_register.place(relx=0.555, rely=0.382, height=54, width=97)
        self.Facial_register.configure(background="#d9d9d8")

        #LOGIN WITH FACE RECOGNITION
        self.Facial_login = tk.Button(self, text='Login via face',command=lambda: self.login_via_face(controller))
        self.Facial_login.place(relx=0.775, rely=0.382, height=54, width=97)
        self.Facial_login.configure(background="#d9d9d8")


    def register(self,controller,with_face = False):
        if self.Name_input.get() != '':
            front_panel.register(self.Name_input.get())
            controller.show_frame(UserPanel)
            user_panel.dig_accounts(Global_var().return_current_id())
            if not with_face:
                popup.popup_message('\tYou need to use your id:\t<<\t{}\t>>\tto login next time\t\t '.format(Global_var().return_current_id()))

            else:
                f_images.make_face_images(40,self.Name_input.get()+'_'+str(Global_var().return_current_id()))
                popup.popup_message('please be patient, now the facial models, are being updated')
                f_train.train()
                popup.popup_message('done')


    def login(self,controller):
        current_user = front_panel.login(self.Name_input.get())
        if user_f.check_for_user(user_id=self.Name_input.get()):
            user_panel.dig_accounts(Global_var().return_current_id())
            if current_user:
                controller.show_frame(UserPanel)

    def login_via_face(self,controller):
        try:
            os.listdir('face_recognition/images/')
            f_iden = identification.identificate()
            Global_var.current_user_id = f_iden[1]
            if user_f.check_for_user(user_id=f_iden[1]):
                user_panel.dig_accounts(Global_var().return_current_id())

                if f_iden[1]:
                    controller.show_frame(UserPanel)
        except:
            print('not anyone registered')


    def add_everyone(self):
        front_panel.money_to_everyone()

    def add_n_users(self):
        front_panel.add_n_users(pl_acc=int(self.Pl_acc_too.getvar(self.var_pl)),eur_acc=int(self.EUR_acc_too.getvar(self.var_eur)))


class Stats(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Statystics", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        controller.geometry("508x292+492+193")

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(UserPanel))
        button1.pack()



class UserPanel(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="User Panel", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        controller.geometry("508x292+492+193")

        self.cb_value = tk.StringVar()

        self.Frame1 = tk.Frame(self)
        self.Frame1.place(relx=0.079, rely=0.206, relheight=0.258, relwidth=0.285)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")

        self.label_name = tk.Label(self,text='Name:')
        self.label_name.place(relx=0.098, rely=0.241, height=21, width=41)

        self.label_id = tk.Label(self,text='Id:')
        self.label_id.place(relx=0.098, rely=0.344, height=21, width=19)

        self.Frame2 = tk.Frame(self)
        self.Frame2.place(relx=0.629, rely=0.206, relheight=0.258, relwidth=0.344)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")

        self.label_number = tk.Label(self.Frame2,text='number:')
        self.label_number.place(relx=0.057, rely=0.133, height=21, width=51)

        self.label_amount = tk.Label(self.Frame2,text='amount')
        self.label_amount.place(relx=0.057, rely=0.533, height=21, width=51)

        self.label_pl_acc = tk.Label(self,text='PL account')
        self.label_pl_acc.place(relx=0.629, rely=0.103, height=21, width=62)

        self.Frame3 = tk.Frame(self)
        self.Frame3.place(relx=0.629, rely=0.584, relheight=0.258, relwidth=0.344)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")

        self.label_eur_acc = tk.Label(self,text='EUR account')
        self.label_eur_acc.place(relx=0.629, rely=0.481, height=21, width=73)

        self.label_eur_number = tk.Label(self,text='number')
        self.label_eur_number.place(relx=0.648, rely=0.619, height=21, width=51)

        self.label_eur_amount = tk.Label(self,text='amount')
        self.label_eur_amount.place(relx=0.648, rely=0.722, height=21, width=51)

        self.Button_log_out = tk.Button(self,text='Log out',command=lambda: self.back_home(controller))
        self.Button_log_out.place(relx=0.432, rely=0.206, height=54, width=77)

        self.Button_add_pl_acc = tk.Button(self, text='+', command=lambda : self.add_acc('PL'))
        self.Button_add_pl_acc.place(relx=0.904, rely=0.103, height=24, width=27)

        self.Button_transfer = tk.Button(self,text='transfer',command=lambda: self.transfer())
        self.Button_transfer.place(relx=0.393, rely=0.756, height=54, width=77)

        self.Entry_number = tk.Entry(self)
        self.Entry_number.place(relx=0.196, rely=0.55, height=20, relwidth=0.244)

        self.Entry_amount = tk.Entry(self)
        self.Entry_amount.place(relx=0.196, rely=0.653, height=20, relwidth=0.244)

        self.Button_add_eur_acc = tk.Button(self,text='+',command=lambda: self.add_acc('EUR'))
        self.Button_add_eur_acc.place(relx=0.904, rely=0.481, height=24, width=27)

        self.Button_delete_pl_acc = tk.Button(self,text='-',command=lambda: self.delete_pl_acc())
        self.Button_delete_pl_acc.place(relx=0.825, rely=0.103, height=24, width=27)

        self.Button_delete_eur_acc = tk.Button(self,text='-',command=lambda: self.delete_eur_acc())
        self.Button_delete_eur_acc.place(relx=0.825, rely=0.481, height=24, width=27)

        self.label_entry_number = tk.Label(self,text='number')
        self.label_entry_number.place(relx=0.079, rely=0.55, height=21, width=48)

        self.label_entry_amount = tk.Label(self,text='amount')
        self.label_entry_amount.place(relx=0.079, rely=0.653, height=21, width=48)

        self.TCombobox1 = ttk.Combobox(self,textvariable='')
        self.TCombobox1['values'] = ('PL','EUR')
        self.TCombobox1.current(0)
        self.TCombobox1.bind("<<ComboboxSelected>>")
        self.TCombobox1.place(relx=0.196, rely=0.756, relheight=0.072, relwidth=0.163)

        self.Button_refresh = tk.Button(self, text='Refresh', command=lambda: self.user_labels())
        self.Button_refresh.place(relx=0.648, rely=0.893, height=24, width=157)

        self.bind("<<ShowFrame>>", self.on_show_frame)

        self.currencies = ['PL','EUR']

    def on_show_frame(self,event):
        self.user_labels()
        self.Entry_amount.delete(0,'end')
        self.Entry_number.delete(0, 'end')

    def transfer(self):
        user_panel.transfer(self.Entry_number.get(),self.Entry_amount.get(),self.currencies[self.TCombobox1.current()])
        #print(self.Entry_number.get(),self.Entry_amount.get(),self.currencies[self.TCombobox1.current()])


    def back_home(self,controller):
        controller.show_frame(StartPage)

    def add_acc(self,currency):
        user_panel.add_account(Global_var().return_current_id(),currency)

    def delete_pl_acc(self):
        user_panel.delete_account(user_f.display_data_user(PL_acc_id=Global_var().return_current_id()),Global_var().return_current_id())

    def delete_eur_acc(self):
        user_panel.delete_account(user_f.display_data_user(EUR_acc_id=Global_var().return_current_id()),Global_var().return_current_id())

    def user_labels(self):
        user_panel.dig_accounts(Global_var().return_current_id())
        self.label_name_out = tk.Label(self, text=user_panel.User_labels().return_var('name'))
        self.label_name_out.place(relx=0.206, rely=0.241, height=21, width=74)
        self.label_name_out.update()

        self.label_id_out = tk.Label(self, text=user_panel.User_labels().return_var('id'))
        self.label_id_out.place(relx=0.206, rely=0.344, height=21, width=74)
        self.label_id_out.update()

        self.label_pl_number_out = tk.Label(self.Frame2, text=user_panel.User_labels().return_var('pl_number'))
        self.label_pl_number_out.place(relx=0.514, rely=0.133, height=21, width=64)
        self.label_pl_number_out.update()

        self.label_pl_amount_out = tk.Label(self.Frame2, text=user_panel.User_labels().return_var('pl_amount'))
        self.label_pl_amount_out.place(relx=0.514, rely=0.533, height=21, width=64)
        self.label_pl_amount_out.update()

        self.label_eur_number_out = tk.Label(self.Frame3, text=user_panel.User_labels().return_var('eur_number'))
        self.label_eur_number_out.place(relx=0.514, rely=0.133, height=21, width=64)
        self.label_eur_number_out.update()

        self.label_eur_amount_out = tk.Label(self.Frame3, text=user_panel.User_labels().return_var('eur_amount'))
        self.label_eur_amount_out.place(relx=0.514, rely=0.533, height=21, width=64)
        self.label_eur_amount_out.update()