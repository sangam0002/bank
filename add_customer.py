from tkinter import*
from tkinter import messagebox
import database

def add_customer_window():
    root = Tk()
    root.title("Add Customer")
    root.geometry("300x350")

    Label(root,text="Add Customer",font=("century",15)).pack(pady=10)

    Label(root,text="Name",font=("century",12)).pack(pady=5)
    name = Entry(root,font=("century",12))
    name.pack(pady=10)

    Label(root,text="Account no",font=("century",12)).pack(pady=5)
    acc_no = Entry(root,font=("century",12))
    acc_no.pack(pady=10)


    Label(root,text="Phone no",font=("century",12)).pack(pady=5)
    mobile = Entry(root,font=("century",12))
    mobile.pack(pady=10)


    def save():
        if name.get == "" or acc_no.get == "" or mobile.get=="":
            messagebox.showerror("Error","fill all fields")
            return
        if database.add_customer(
            name.get(),
            acc_no.get(),
            mobile.get()):

            messagebox.showinfo("success","customer added")

        name.delete(0,END)
        acc_no.delete(0,END)
        mobile.delete(0,END) 

    Button(root,text="save",command=save).pack()

    root.mainloop()