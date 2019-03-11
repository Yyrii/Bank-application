import tkinter as tk
import tkinter.ttk as ttk
import sql_operations.user_functions as user_f
from sql_operations.global_variables import*
import backend.user_panel as user_panel

LARGE_FONT = ("Verdana", 12)

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Bank system", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        controller.geometry("508x292+492+193")

        #SHOW STATS BUTTON
        Show_stats = tk.Button(self, text="Show stats",
            command=lambda: [controller.show_frame(Stats),printer(user_name.get())])#controller.geometry("808x292+492+193"))#printer(user_name.get()))
        Show_stats.configure(background="#d9d9d8")
        Show_stats.place(relx=0.079, rely=0.685, height=54, width=97)

        #USER NAME INPUT
        user_name = tk.StringVar()
        Name_input = tk.Entry(self,textvariable=user_name)
        Name_input.place(relx=0.079, rely=0.271, height=20, relwidth=0.382)

        #TEXT ABOVE INPUT
        Name = ttk.Label(self)
        Name.place(relx=0.079, rely=0.168, height=19, width=116)
        Name.configure(text='Name')

        #LOGIN BUTTON
        Log_in_b = tk.Button(self,text='Log in',
            command=lambda: dodaj())
        Log_in_b.place(relx=0.079, rely=0.382, height=54, width=97)
        Log_in_b.configure(background="#d9d9d8")

        #REGISTER BUTTON
        Register_b = tk.Button(self,text='Register')
        Register_b.place(relx=0.315, rely=0.382, height=54, width=97)
        Register_b.configure(background="#d9d9d8")

def dodaj():
    user_f.add_user('Users','andrir')

class Stats(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Statystics", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        controller.geometry("508x292+492+193")

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(UserPanel))
        button1.pack()


def printer(arg):
    print(arg)

def printer_test(cos):
    return cos

class UserPanel(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="User Panel", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        controller.geometry("508x292+492+193")


        Frame1 = tk.Frame(self)
        Frame1.place(relx=0.079, rely=0.206, relheight=0.258, relwidth=0.285)
        Frame1.configure(relief='groove')
        Frame1.configure(borderwidth="2")

        label_name = tk.Label(self,text='Name:')
        label_name.place(relx=0.098, rely=0.241, height=21, width=41)

        label_id = tk.Label(self,text='Id:')
        label_id.place(relx=0.098, rely=0.344, height=21, width=19)

        label_name_out = tk.Label(self, text=user_panel.Optional_labels.label_name_out)
        label_name_out.place(relx=0.236, rely=0.241, height=21, width=34)

        label_id_out = tk.Label(self,text=user_panel.Optional_labels.label_id_out)
        label_id_out.place(relx=0.236, rely=0.344, height=21, width=34)

        Frame2 = tk.Frame(self)
        Frame2.place(relx=0.629, rely=0.206, relheight=0.258, relwidth=0.344)
        Frame2.configure(relief='groove')
        Frame2.configure(borderwidth="2")

        label_number = tk.Label(Frame2,text='number:')
        label_number.place(relx=0.057, rely=0.133, height=21, width=51)

        label_amount = tk.Label(Frame2,text='amount')
        label_amount.place(relx=0.057, rely=0.533, height=21, width=51)

        label_pl_number_out = tk.Label(Frame2,text=user_panel.Optional_labels.label_pl_number_out)
        label_pl_number_out.place(relx=0.514, rely=0.133, height=21, width=64)

        label_pl_amount_out = tk.Label(Frame2,text=user_panel.Optional_labels.label_pl_amount_out)
        label_pl_amount_out.place(relx=0.514, rely=0.533, height=21, width=34)

        label_pl_acc = tk.Label(self,text='PL account')
        label_pl_acc.place(relx=0.629, rely=0.103, height=21, width=62)

        Frame3 = tk.Frame(self)
        Frame3.place(relx=0.629, rely=0.584, relheight=0.258, relwidth=0.344)
        Frame3.configure(relief='groove')
        Frame3.configure(borderwidth="2")

        label_eur_number_out = tk.Label(Frame3,text=user_panel.Optional_labels.label_eur_number_out)
        label_eur_number_out.place(relx=0.514, rely=0.133, height=21, width=34)

        label_eur_amount_out = tk.Label(Frame3,text=user_panel.Optional_labels.label_eur_amount_out)
        label_eur_amount_out.place(relx=0.514, rely=0.533, height=21, width=34)

        label_eur_acc = tk.Label(self,text='EUR account')
        label_eur_acc.place(relx=0.629, rely=0.481, height=21, width=73)

        label_eur_number = tk.Label(self,text='number')
        label_eur_number.place(relx=0.648, rely=0.619, height=21, width=51)

        label_eur_amount = tk.Label(self,text='amount')
        label_eur_amount.place(relx=0.648, rely=0.722, height=21, width=51)

        Button_log_out = tk.Button(self,text='Log out')
        Button_log_out.place(relx=0.432, rely=0.206, height=54, width=77)

        Button_add_pl_acc = tk.Button(self,text='+')
        Button_add_pl_acc.place(relx=0.904, rely=0.103, height=24, width=27)

        Button_transfer = tk.Button(self,text='transfer')
        Button_transfer.place(relx=0.393, rely=0.756, height=54, width=77)

        Entry_number = tk.Entry(self)
        Entry_number.place(relx=0.196, rely=0.55, height=20, relwidth=0.244)

        Entry_amount = tk.Entry(self)
        Entry_amount.place(relx=0.196, rely=0.653, height=20, relwidth=0.244)

        Button_add_eur_acc = tk.Button(self,text='+')
        Button_add_eur_acc.place(relx=0.904, rely=0.481, height=24, width=27)

        Button_delete_pl_acc = tk.Button(self,text='-')
        Button_delete_pl_acc.place(relx=0.825, rely=0.103, height=24, width=27)

        Button_delete_eur_acc = tk.Button(self,text='-')
        Button_delete_eur_acc.place(relx=0.825, rely=0.481, height=24, width=27)

        label_entry_number = tk.Label(self,text='number')
        label_entry_number.place(relx=0.079, rely=0.55, height=21, width=48)

        label_entry_amount = tk.Label(self,text='amount')
        label_entry_amount.place(relx=0.079, rely=0.653, height=21, width=48)

        TCombobox1 = ttk.Combobox(self,textvariable='')
        TCombobox1.place(relx=0.196, rely=0.756, relheight=0.072
                              , relwidth=0.163)

        Button_refresh = tk.Button(self,text='Refresh')
        Button_refresh.place(relx=0.648, rely=0.893, height=24, width=157)