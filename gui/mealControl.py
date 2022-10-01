import tkinter as tk
from tkinter import ttk

import sys
 
# setting path
sys.path.append('../musikVereinKassePython')

from logic.dining.meal import Meal

class MealControl:
    def __init__(self, root, meal):
        self._root = root
        self._frame = ttk.Frame(root, padding=10)
        self._meal = meal

        def valueChanged():
            print(self._spinbox.get()) 

        self._spinbox = ttk.Spinbox(
            self._frame,
            from_=0, increment=1, to=100, 
            textvariable=tk.StringVar(value=0), 
            command=valueChanged)
        self._spinbox.grid(column=0, row=0)
        self._frame.pack()
        s = ttk.Style(self._frame)
        s.configure('TFrame', background="red")



if __name__ == "__main__":
    root = tk.Tk()

    m = MealControl(root, Meal(0, "name", 5.20))

    root.mainloop()

