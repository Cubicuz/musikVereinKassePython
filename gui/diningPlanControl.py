import tkinter as tk
from tkinter import ttk

# setting path
if __name__ == "__main__":
    import sys
    sys.path.append('../musikVereinKassePython')

from mealControl import MealControl
from logic.dining.diningPlan import DiningPlan

def createStyle(styleName, color):
    s = ttk.Style()
    s.configure(styleName+'.TFrame', background=color)
    s.configure(styleName+'.TLabel', background=color)

class diningPlanControl:



    def __init__(self, root, dp):
        self._diningPlan = dp
        self._mealControls = []
        self._frame = ttk.Frame(root, padding=5)
        for mg in dp.mealGroups:
            print(mg.name)
            createStyle(mg.name, mg.color)
            for m in mg.meals:
                mc = MealControl(self._frame, m, mg.name)
                self._mealControls.append(mc)
        self._frame.pack()




if __name__ == "__main__":
    root = tk.Tk()

    dp = DiningPlan.generateMock()

    diningPlanControl(root, dp)

    root.mainloop()

