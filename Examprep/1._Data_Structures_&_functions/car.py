class Car:

    def __init__(self, make, model, year, type, price):
        self.make = make
        self.model = model
        self.year = year
        self.type = type
        self.price = price

    def __repr__(self):
        return f'Make: {self.make}, Model: {self.model}, Car type: {self.type}'