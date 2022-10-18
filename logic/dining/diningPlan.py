from logic.event import Event
from logic.dining.mealGroup import MealGroup

class DiningPlan:

    def __init__(self, mealGroups):
        self._mealGroups = mealGroups
        self._price = 0
        self.priceChanged = Event()

    def get_mealGroups(self):
        return self._mealGroups
    mealGroups = property(get_mealGroups)

    def get_price(self):
        return self._price
    def set_price(self, price):
        if self._price != price:
            self._price = price
            self.priceChanged(price)
    price = property(get_price, set_price)

    def resetOrder(self):
        for mg in self._mealGroups:
            for m in mg.meals:
                m.amount = 0

    def payOrder(self):
        for mg in self._mealGroups:
            for m in mg.meals:
                m.payOrder()

        #TODO store order

    def generateMock():
        mealGroups = []
        for i in range(3):
            mealGroups.append(MealGroup.generateMock(i))
        return DiningPlan(mealGroups)

