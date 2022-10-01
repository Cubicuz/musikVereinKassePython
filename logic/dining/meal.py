from logic.event import Event
from decimal import *

#decimals need 2 significant places
getcontext().prec = 2

class Meal:


    def __init__(self, id, name, price, totalAmount = 0):
        self._id = id
        self._name = name
        self._price = Decimal(price)
        self._amount = 0
        self._totalAmount = totalAmount

        #events
        self._amountChanged = Event()

    def changeAmount(self, diffAmount):
        if diffAmount != 0:
            self._amount += diffAmount
            self._amountChanged(diffAmount)
    def get_amount(self):
        return self._amount
    def set_amount(self, val):
        if self._amount != val:
            diff = val - self._amount
            self._amount = val
            self._amountChanged(diff)
    amount = property(get_amount, set_amount)

    def get_totalAmount(self):
        return self._totalAmount
    totalAmount = property(get_totalAmount)

    def get_name(self):
        return self._name
    name = property(get_name)

    def get_price(self):
        return self._price
    price = property(get_price)

    def payOrder(self):
        if self._amount != 0:
            self._totalAmount += self._amount
            self.amount = 0
