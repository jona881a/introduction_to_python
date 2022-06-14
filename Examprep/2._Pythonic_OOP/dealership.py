class Dealership:
    
    def __init__(self):
        self.carInventory = []
        
    def __add__(self, car): #normalt virker + ikke med lister men her gør den fordi vi definere den
        self.carInventory.append(car)

    def __str__(self):
        for i in range(len(self.carInventory)):
            dict(self.carInventory[i])
