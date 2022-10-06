import tkinter as tk
from tkinter import ttk

# setting path
if __name__ == "__main__":
    import sys
    sys.path.append('../musikVereinKassePython')

from logic.dining.meal import Meal

# Validating function
def numberValidator(user_input):
    # check if the input is numeric
    if  user_input.isdigit():
        # Fetching minimum and maximum value of the spinbox
        minval = int(0)
        maxval = int(1000)

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

    def __init__(self, root, meal, styleName):
        self._root = root
        self._meal = meal
        self._amount = tk.IntVar(value=0)

        def entryChanged(*args):
            if self._meal.amount != self._amount.get():
                self._meal.amount = self._amount.get() 
        self._amount.trace_add("write", entryChanged)

        def clickHandler(event):
            print(event.num)
            if event.num == 1: # left click
                print('increment')
                self._meal.changeAmount(1)
            if event.num == 3: # right click
                print('decrement')
                self._meal.changeAmount(-1)
            print(self._meal.amount)

        def amountChangedHandler(amount):
            print("amount changed " + str(amount))
            if (self._amount != amount):
                self._amount.set(amount)
            

        self._frame = ttk.Frame(
            root, 
            padding=10,
            style=styleName+'.TFrame')
        self._frame.bind("<Button>", clickHandler)

        self._label = ttk.Label(
            self._frame,
            text=self._meal.name,
            style=styleName+'.TLabel')
        self._label.grid(column=0, row=0)
        self._label.bind("<Button>", clickHandler)

        self._spinbox = ttk.Spinbox(
            self._frame,
            from_=0, increment=1, to=1000, 
            textvariable=self._amount)
        self._spinbox.grid(column=1, row=0)
        self._meal.amountChanged += amountChangedHandler


        self._frame.pack()
        self._frame.config(style=styleName + '.TFrame')

        validator = self._frame.register(numberValidator)
        self._spinbox.config(validate="key", validatecommand=(validator, '%P'))



if __name__ == "__main__":
    root = tk.Tk()

    s = ttk.Style()
    styleName = 'Group1'
    s.configure(styleName+'.TFrame', background="green")
    s.configure(styleName+'.TLabel', background="green")

    m = MealControl(root, Meal(0, "name", 5.20), styleName)

    root.mainloop()

