from car import Car;
import datetime, csv;
from datastructure_tools import find_same_names

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

try:
  dealership.sort()
except TypeError:
  print("can't compare cars")

print("\nSorting using .sort()")
print([car.__dict__ for car in dealership])

print("\nSorting with sorted by make")
sortedDealership = sorted(dealership, key=sortByAttributeMake)
print([car.make for car in sortedDealership])

print("\nLambda sorted key: ")
sortedDealership = sorted(dealership, key=lambda car: car.price)
print([(car.make, car.price) for car in sortedDealership])

with open("names.csv",'r') as file:
  csvreader = csv.reader(file)

  headers = next(csvreader) #Headers er ligegyldige her

  rows = [row for row in csvreader]
  names = []

  for col in rows:
    names.append(col[headers.index("first_name")])
  
  print(find_same_names(names))
  #flatten_matrix = [row for sublist in csvreader for row in sublist]
  #print(flatten_matrix)