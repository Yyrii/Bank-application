import tkinter as tk
import tkinter.ttk as ttk



def popup_message(msg):
    popup = tk.Tk()
    label = ttk.Label(popup,text=msg)
    label.pack()
    Ok_button = ttk.Button(popup,text='Okay',command=lambda :popup.destroy())
    Ok_button.pack()
    popup.mainloop()