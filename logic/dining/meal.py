from event import Event

class Meal:


    def __init__(self, id, name, price, halfPrice = 0, totalAmount = 0, totalHalfAmount = 0):
        self._id = id
        self._name = name
        self._price = price
        self._halfPrice = halfPrice
        self._amount = 0
        self._amountChanged = Event()
        self._amountHalfPrice = 0
        self._totalAmount = totalAmount
        self._totalHalfAmount = totalHalfAmount

    def changeAmount(self, diffAmount):
        pass

    def get_amount(self):
        return self._amount
    def set_amount(self, amount):
        diff = amount - self._amount
        self._amount = amount
        self._amountChanged()
    amount = property(get_amount, set_amount)



