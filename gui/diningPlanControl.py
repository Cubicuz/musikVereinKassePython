import tkinter as tk
from tkinter import ttk

# setting path
if __name__ == "__main__":
    import sys
    sys.path.append('../musikVereinKassePython')

from mealControl import MealControl
from logic.dining.diningPlan import DiningPlan

class diningPlanControl:
    def __init__(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()

    s = ttk.Style()
    styleName = 'Group1'
    s.configure(styleName+'.TFrame', background="green")
    s.configure(styleName+'.TLabel', background="green")

    dp = DiningPlan.generateMock()

    root.mainloop()

