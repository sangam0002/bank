from tkinter import*
import database


def customer_list_window():
    

    root = Tk()
    root.title("customer list")
    root.geometry("600x400")
    

    listbox = Listbox(root,width=60,height=15)
    listbox.pack(pady=20)

    customers = database.show_customer()

    for customer in customers:
        listbox.insert(END,f"{customer[0]} -- {customer[1]} -- {customer[2]} ")

    root.mainloop()
