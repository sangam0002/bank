from tkinter import *
from tkinter import messagebox
import database

def delete_customer_window():
    root=Tk()
    root.title("Delete customer")
    root.geometry("250x300")

    Label(root,text="Enter Customer Id").pack(pady=10)

    id_entry=Entry(root)
    id_entry.pack()

    def delete():
        database.delete_customer(id_entry.get())
        messagebox.showinfo("success","customer deleted")


    Button(root,text="Delete",command=delete).pack(pady=10)

    root.mainloop()