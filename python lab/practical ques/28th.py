# 28) Write a python script to create GUI for basic mathematical operations. 



import tkinter as tk

def add():
    result.config(text="Result: " + str(int(e1.get()) + int(e2.get())))

def subtract():
    result.config(text="Result: " + str(int(e1.get()) - int(e2.get())))

def multiply():
    result.config(text="Result: " + str(int(e1.get()) * int(e2.get())))

def divide():
    result.config(text="Result: " + str(int(e1.get()) / int(e2.get())))

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x300")

tk.Label(root, text="Enter First Number").pack()
e1 = tk.Entry(root)
e1.pack()

tk.Label(root, text="Enter Second Number").pack()
e2 = tk.Entry(root)
e2.pack()

tk.Button(root, text="Addition (+)", command=add).pack(pady=5)
tk.Button(root, text="Subtraction (-)", command=subtract).pack(pady=5)
tk.Button(root, text="Multiplication (*)", command=multiply).pack(pady=5)
tk.Button(root, text="Division (/)", command=divide).pack(pady=5)

result = tk.Label(root, text="Result: ")
result.pack(pady=10)

root.mainloop()