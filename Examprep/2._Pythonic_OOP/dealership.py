class Dealership:
    
    def __init__(self):
        self.carInventory = []
        
    def __add__(self, car):
        self.carInventory.append(car)

    def __str__(self):
        for i in range(len(self.carInventory)):
            dict(self.carInventory[i])
