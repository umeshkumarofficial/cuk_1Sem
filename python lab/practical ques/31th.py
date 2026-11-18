# 31) Write a Python script that reads student marks from a CSV data file, analyzes the information, and outputs the results using GUI.


import tkinter as tk
from tkinter import filedialog
import pandas as pd

def open_file():
    file = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if file:
        data = pd.read_csv(file)

        total = data["Marks"].sum()
        average = data["Marks"].mean()
        highest = data["Marks"].max()

        result.config(text=
            "Total Marks: " + str(total) +
            "\nAverage Marks: " + str(average) +
            "\nHighest Marks: " + str(highest)
        )

root = tk.Tk()
root.title("Student Marks Analysis")
root.geometry("350x250")

tk.Label(root, text="Student Marks Analysis",
         font=("Arial", 14, "bold")).pack(pady=15)

tk.Button(root, text="Open CSV File",
          command=open_file).pack(pady=10)

result = tk.Label(root, text="Results will appear here")
result.pack(pady=20)

root.mainloop()
