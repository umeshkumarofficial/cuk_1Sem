# 29) Write a python script to read CSV data file and visualize data in charts by using GUI.


import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt

def open_file():
    file = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if file:
        data = pd.read_csv(file)

        data.plot(kind='bar')
        plt.title("CSV Data Visualization")
        plt.show()

root = tk.Tk()
root.title("CSV Data Visualization")
root.geometry("300x200")

tk.Label(root, text="CSV Data Visualization",
         font=("Arial", 14)).pack(pady=20)

tk.Button(root, text="Open CSV File",
          command=open_file).pack(pady=20)

root.mainloop()
