# 30) Write a python script to Create login form using GUI.


import tkinter as tk
from tkinter import messagebox

def login():
    username = e1.get()
    password = e2.get()

    if username == "admin" and password == "1234":
        messagebox.showinfo("Login", "Login Successful")
    else:
        messagebox.showerror("Login", "Invalid Username or Password")

root = tk.Tk()
root.title("Login Form")
root.geometry("300x250")

tk.Label(root, text="Login Form",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Username").pack()
e1 = tk.Entry(root)
e1.pack()

tk.Label(root, text="Password").pack()
e2 = tk.Entry(root, show="*")
e2.pack()

tk.Button(root, text="Login", command=login).pack(pady=15)

root.mainloop()
