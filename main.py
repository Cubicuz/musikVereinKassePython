import tkinter as tk
from tkinter import ttk

from logic.dining.meal import Meal
from gui.mealControl import MealControl

import sys

print(sys.path)

root = tk.Tk()

s = ttk.Style()
styleName = 'Group1'
s.configure(styleName+'.TFrame', background="green")
s.configure(styleName+'.TLabel', background="green")
meal = Meal(1, "Döner", 3.50)
mc = MealControl(root, meal, styleName)


txt = ttk.Label(root, text="Welcome to GeekForGeeks")
txt.pack()

root.mainloop()