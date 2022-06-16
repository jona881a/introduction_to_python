from this import d
from car import Car;
import datetime;

def sortByAttributeMake(car):
  return car.make

dealership = [
  Car('Ford','Mustang',datetime.datetime(1969, 1, 1),'Musclecar', 800000), 
  Car('Nissan','Skyline R34', datetime.datetime(2000, 1, 1), 'Tuner', 450000), 
  Car('Ford','GT',datetime.datetime(2010,2,10),'Supercar',3200000), 
  Car('Bugatti','Veyron 16.4',datetime.datetime(2012,10,10),'Hypercar',12000000)
]

for i in range(len(dealership)):
  print(dealership[i].__dict__)

dealership.sort()

print("\nSorting using .sort()")
print([car.__dict__ for car in dealership])

print("\nSorting with sorted by make")
sortedDealership = sorted(dealership, key=sortByAttributeMake)
print([car.make for car in sortedDealership])

print("\n Inline sorted key: ")
sortedDealership = sorted(dealership, key=lambda car: car.price)
print([(car.make, car.price) for car in sortedDealership])
"""
print("Purchase a new Car")
print("\n Searching for at specific value: ")
input = input("What would you like to see? ")

while i < len(dealership):
  if dealership[i]
else:
  print("\n Sorry but i couldn't find anything that matched your request")
"""