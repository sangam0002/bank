from tkinter import*
from tkinter import messagebox
import database 

def deposit_window():
    root = Tk()
    root.title("Deposit Money")
    root.geometry("300x350")

    Label(root,text="Deposit Money",font=("century",15)).pack(pady=10)

    Label(root,text="Account no",font=("century",15)).pack(pady=5)
    acc_no = Entry(root)
    acc_no.pack(pady=10)

    Label(root,text="Amount",font=("century",15)).pack(pady=5)
    amount = Entry(root)
    amount.pack(pady=10)

    def deposit_money():
        if acc_no.get =="" or acc_no.get == "":
            messagebox.showerror("error","fill all fields")
            return

        database.deposit(acc_no,float(amount))
        messagebox.showinfo("success","amount deposit successfilly")

        acc_no.delete(0,END)
        amount.delete(0,END)

    Button(root,text="deposit",command=deposit_money).pack()

    root.mainloop()