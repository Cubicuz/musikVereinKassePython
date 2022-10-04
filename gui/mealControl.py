import tkinter as tk
from tkinter import ttk

import sys
 
# setting path
sys.path.append('../musikVereinKassePython')

from logic.dining.meal import Meal

# Validating function
def numberValidator(user_input):
    # check if the input is numeric
    if  user_input.isdigit():
        # Fetching minimum and maximum value of the spinbox
        minval = int(0)
        maxval = int(100)
 
        # check if the number is within the range
        if int(user_input) not in range(minval, maxval):
            print ("Out of range")
            return False
 
        # Printing the user input to the console
        print(user_input)
        return True
 
    # if input is blank string
    elif user_input == "":
        print(user_input)
        return True
 
    # return false is input is not numeric
    else:
        print("Not numeric ", user_input)
        return False

class MealControl:
    def __init__(self, root, meal):
        self._root = root
        self._frame = ttk.Frame(root, padding=10)
        self._meal = meal
        self._amount = tk.IntVar(value=0)
        def valueChanged():
            print(self._amount.get()) 

        self._spinbox = ttk.Spinbox(
            self._frame,
            from_=0, increment=1, to=100, 
            textvariable=self._amount, 
            command=valueChanged)
        self._spinbox.grid(column=0, row=0)
        self._frame.pack()
        s = ttk.Style(self._frame)
        s.configure('TFrame', background="red")

        validator = self._frame.register(numberValidator)
        self._spinbox.config(validate="key", validatecommand=(validator, '%P'))



if __name__ == "__main__":
    root = tk.Tk()

    m = MealControl(root, Meal(0, "name", 5.20))

    root.mainloop()

