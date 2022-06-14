from car import Car;
import datetime;

dealership = [
  Car('Ford','Mustang',datetime.datetime(1969, 1, 1),'Musclecar', 800000), 
  Car('Nissan','Skyline R34', datetime.datetime(2000, 1, 1), 'Tuner', 450000), 
  Car('Ford','GT',datetime.datetime(2010,2,10),'Supercar',3200000), 
  Car('Bugatti','Veyron 16.4',datetime.datetime(2012,10,10),'Hypercar',12000000)
]

for i in range(len(dealership)):
  print(dealership[i].__dict__)