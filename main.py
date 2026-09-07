from tkinter import *


import database
import add_customer
import customer_list
import delete_customer
import deposit_money
import withdraw_money
import check_balance


database.connect()

root = Tk()
root.title("Student Data")
root.geometry("300x400")

Label(root,text="Bank Management",font=("segoe ui",15,"bold")).pack(pady=10)

Button(root,text="add customer",
       command=add_customer.add_customer_window
       ).pack(pady=10)

Button(root,text="customer list",
       width=20,
       command=customer_list.customer_list_window
       ).pack(pady=10)

Button(root,text="delete customer",width=20,
       command=delete_customer.delete_customer_window).pack(pady=10)


Button(root,text="deposit money",width=20,
       command=deposit_money.deposit_window).pack(pady=10)

Button(root,text="withdraw money",width=20,
       command=withdraw_money.withdraw_window).pack(pady=10)

Button(root,text="check balance",width=20,
       command=check_balance.balance_window).pack(pady=10)

root.mainloop()

  