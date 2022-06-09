from dealership import Dealership
from car import Car
import datetime

dealership = Dealership()

dealership + Car('Ford','Mustang',datetime.datetime(1969, 1, 1),'Musclecar', 800000)

dealership + Car('Nissan','Skyline R34', datetime.datetime(2000, 1, 1), 'Tuner', 450000)

str(dealership)
