import sqlite3

def connect():
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()


    cursor.execute("""CREATE TABLE IF NOT EXISTS accounts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    account_no TEXT UNIQUE,
    mobile TEXT
    )
""")
    conn.commit()
    conn.close()



def add_customer(name,account_no,mobile,):
    conn =sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO accounts(name,account_no,mobile) VALUES(?,?,?)",
                   (name,account_no,mobile))
    conn.commit()
    conn.close()


def show_customer():
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM accounts")
    data = cursor.fetchall()

    conn.commit()
    conn.close()
    return data


def delete_customer(id):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM accounts WHERE id=?",(id))

    conn.commit()
    conn.close()


def deposit(account_no,amount):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE accounts SET balance = balance + ? WHERE account_no=?",(account_no,amount))

    conn.commit()
    conn.close()


def withdraw(account_no,amount):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()
    
    cursor.execute("UPDATE accounts SET balance = balance - ? WHERE account_no=?",(account_no,amount))
    
    conn.commit()
    conn.close()

def check_balance(account_no):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute("SELECT balance FROM accounts WHERE account_no=?",(account_no))
    data = cursor.fetchone()

    conn.commit()
    conn.close()
    return data

