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
    user_f.add_user('Users',123,'efwwe')

class Stats(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Statystics", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        controller.geometry("508x292+492+193")

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()




def printer(arg):
    print(arg)

