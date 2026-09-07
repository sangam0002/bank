from tkinter import *
from tkinter import messagebox
import database


def balance_window():
    root = Tk()
    root.title("Check Balance")
    root.geometry("300x350")

    Label(root,text="check balance",font=("century",15)).pack(pady=10)

    Label(root,text="check balance",font=("century",15)).pack(pady=10)
    acc_no = Entry(root)
    acc_no.pack(pady=10)

    def check_balance():
        if acc_no.get()=="":
            messagebox.showerror("error","enter account number")
            return
        data = database.check_balance(acc_no)


    Button(root,text="check balance",command=check_balance).pack(pady=10)

    root.mainloop()
