import tkinter as tk
import tkinter.ttk as ttk
import sql_operations.user_functions as user_f

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

        Label1 = tk.Label(self,text='Name:')
        Label1.place(relx=0.098, rely=0.241, height=21, width=41)

        Label2 = tk.Label(self,text='Id:')
        Label2.place(relx=0.098, rely=0.344, height=21, width=19)

        Label3 = tk.Label(self,text='')
        Label3.place(relx=0.236, rely=0.241, height=21, width=34)

        Label4 = tk.Label(self,text='')
        Label4.place(relx=0.236, rely=0.344, height=21, width=34)

        Frame2 = tk.Frame(self)
        Frame2.place(relx=0.629, rely=0.206, relheight=0.258, relwidth=0.344)
        Frame2.configure(relief='groove')
        Frame2.configure(borderwidth="2")

        Label6 = tk.Label(Frame2,text='number:')
        Label6.place(relx=0.057, rely=0.133, height=21, width=51)

        Label7 = tk.Label(Frame2,text='amount')
        Label7.place(relx=0.057, rely=0.533, height=21, width=51)

        Label3_3 = tk.Label(Frame2,text='')
        Label3_3.place(relx=0.514, rely=0.133, height=21, width=34)

        Label3_4 = tk.Label(Frame2,text='')
        Label3_4.place(relx=0.514, rely=0.533, height=21, width=34)

        Label5 = tk.Label(self,text='PL account')
        Label5.place(relx=0.629, rely=0.103, height=21, width=62)

        Frame3 = tk.Frame(self)
        Frame3.place(relx=0.629, rely=0.584, relheight=0.258, relwidth=0.344)
        Frame3.configure(relief='groove')
        Frame3.configure(borderwidth="2")

        Label3_5 = tk.Label(Frame3,text='')
        Label3_5.place(relx=0.514, rely=0.133, height=21, width=34)

        Label3_6 = tk.Label(Frame3,text='')
        Label3_6.place(relx=0.514, rely=0.533, height=21, width=34)

        Label8 = tk.Label(self,text='EUR amount')
        Label8.place(relx=0.629, rely=0.481, height=21, width=73)

        Label6_1 = tk.Label(self,text='number')
        Label6_1.place(relx=0.648, rely=0.619, height=21, width=51)

        Label7_2 = tk.Label(self,text='amount')
        Label7_2.place(relx=0.648, rely=0.722, height=21, width=51)

        Button1 = tk.Button(self,text='Log out')
        Button1.place(relx=0.432, rely=0.206, height=54, width=77)

        Button2 = tk.Button(self,text='+')
        Button2.place(relx=0.904, rely=0.103, height=24, width=27)

        Button3 = tk.Button(self,text='transfer')
        Button3.place(relx=0.393, rely=0.756, height=54, width=77)

        Entry1 = tk.Entry(self)
        Entry1.place(relx=0.196, rely=0.55, height=20, relwidth=0.244)

        Entry2 = tk.Entry(self)
        Entry2.place(relx=0.196, rely=0.653, height=20, relwidth=0.244)

        Button2_7 = tk.Button(self,text='+')
        Button2_7.place(relx=0.904, rely=0.481, height=24, width=27)

        Button2_8 = tk.Button(self,text='-')
        Button2_8.place(relx=0.825, rely=0.103, height=24, width=27)

        Button2_9 = tk.Button(self,text='-')
        Button2_9.place(relx=0.825, rely=0.481, height=24, width=27)

        Label9 = tk.Label(self,text='number')
        Label9.place(relx=0.079, rely=0.55, height=21, width=48)

        Label10 = tk.Label(self,text='amount')
        Label10.place(relx=0.079, rely=0.653, height=21, width=48)

        TCombobox1 = ttk.Combobox(self,textvariable='')
        TCombobox1.place(relx=0.196, rely=0.756, relheight=0.072
                              , relwidth=0.163)

        Button4 = tk.Button(self,text='Refresh')
        Button4.place(relx=0.648, rely=0.893, height=24, width=157)