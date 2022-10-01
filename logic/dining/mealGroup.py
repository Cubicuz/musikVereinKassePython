from meal import Meal


class MealGroup:
    def __init__(self, meals, name, color, tab = "0"):
        self._meals = meals
        self._name = name
        self._color = color
        self._tab = tab

    def get_tab(self):
        return self._tab
    tab = property(get_tab)

    def get_name(self):
        return self._name
    name = property(get_name)

    def get_color(self):
        return self._color
    color = property(get_color)

    def get_meals(self):
        return self._meals
    meals = property(get_meals)