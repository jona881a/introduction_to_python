from car import Car;
import datetime, csv;
from datastructure_tools import *

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

print("\nSorted with Lambda for price ")
sortedDealership = sorted(dealership, key=lambda car: car.price, reverse=True)
print([(car.make, car.model ,car.price) for car in sortedDealership])


print("\nFinding how many occurences of Names in names.csv")
print(find_occurences_of_attribute("names.csv", "first_name"))

print("\nWith cardata.csv and car_make as attribute")
car_make_dict = find_occurences_of_attribute("../testdata/cardata.csv", "car_make")

print("\nSorted after highest count")
sorted_dict = sorted(car_make_dict.items(), key=lambda item: item[1], reverse=True)
print(sorted_dict)

print("\nFinding the make with the most cars represented")
print(max_occurence(car_make_dict))

#flatten_matrix = [row for sublist in csvreader for row in sublist]
#print(flatten_matrix)