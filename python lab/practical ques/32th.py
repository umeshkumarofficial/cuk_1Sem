# 32) Write a Python script that demonstrate menu and progress bar controls of GUI.


import tkinter as tk
from tkinter import ttk

def start():
    progress.start(10)

def stop():
    progress.stop()

root = tk.Tk()
root.title("Menu and Progress Bar")
root.geometry("300x200")

# Create Menu
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Start", command=start)
file_menu.add_command(label="Stop", command=stop)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

# Create Progress Bar
tk.Label(root, text="Progress Bar").pack(pady=15)

progress = ttk.Progressbar(root, length=200, mode="indeterminate")
progress.pack(pady=10)

tk.Button(root, text="Start", command=start).pack()
tk.Button(root, text="Stop", command=stop).pack()

root.mainloop()
