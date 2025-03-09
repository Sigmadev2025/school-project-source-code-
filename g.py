from p import *
from tkinter import messagebox
import tkinter as tk

scr = tk.Tk()

def logi():
    try:
        m = password.get()
        z = j.get()
        if check(z, m) == True:
            if data[z][2] == "student":
                student(z)
                tk.mainloop()
            if data[z][2] == "admin":
                admin(z)
        else:
            messagebox.showerror("Login Error", "Could not find given username or password")
    except KeyError:
        messagebox.showerror("Login Error", "Invalid username")

def signup():
    s = entry1.get()
    p = entry2.get()
    r = entry3.get()
    data.setdefault(s, (s, p, r, 9.0))  

def signup2():
    signup()
    messagebox.showinfo("Signup", "Signed up successfully")        

def student(usera):
    roo = tk.Toplevel()
    balance = data[usera][3]
    username = data[usera][0]

    tk.Label(roo, text=f"Welcome {username}").pack(pady=5)
    tk.Label(roo, text="Withdraw").pack(pady=5)

    def withdrawappt():
        amoun = int(entry.get())
        if withdraw(usera, amoun):
            b.config(text=f"Balance: {getbalance(usera)} DenDollars")
            messagebox.showinfo("Success", f"Withdrawn {amoun} DenDollars")
        else:
            messagebox.showerror("Error", "Insufficient balance")

    entry = tk.Entry(roo)
    entry.pack()
    tk.Button(roo, text="Withdraw", command=withdrawappt).pack()
    
    b = tk.Label(roo, text=f"Balance {balance}")
    b.pack(pady=5)

def admin(user):
    root = tk.Toplevel()
    username = data[user][0]
    
    tk.Label(root, text=f"Welcome {username}").pack(pady=5)
    tk.Label(root, text="Choose student").pack(pady=5)

    global entry
    entry = tk.Entry(root)
    entry.pack()

    tk.Label(root, text="Enter amount").pack(pady=5)

    global entryb
    entryb = tk.Entry(root)
    entryb.pack()

    tk.Button(root, text="Fund Wallet", command=fund_wallet).pack(pady=5)

def fund_wallet():
    student_name = entry.get()
    amount = int(entryb.get())
    if student_name in data:
        data[student_name] = (data[student_name][0], data[student_name][1], data[student_name][2], data[student_name][3] + amount)
        messagebox.showinfo("Success", f"Funded {amount} DenDollars to {student_name}")
    else:
        messagebox.showerror("Error", "Student not found")

tk.Label(scr, text="Login").pack(pady=5)
j = tk.Entry(scr)
j.pack()

tk.Label(scr, text="Password").pack(pady=5)
password = tk.Entry(scr, show="*")
password.pack()

tk.Button(scr, text="Login", command=logi).pack()
tk.Label(scr, text="Signup").pack(pady=5)

tk.Label(scr, text="Username").pack(pady=5)
entry1 = tk.Entry(scr)
entry1.pack()

tk.Label(scr, text="Password").pack(pady=5)
entry2 = tk.Entry(scr, show="*")
entry2.pack()

tk.Label(scr, text="Role in school (student or admin)").pack(pady=5)
entry3 = tk.Entry(scr)
entry3.pack()

tk.Button(scr, text="Signup", command=signup2).pack()

tk.mainloop()
