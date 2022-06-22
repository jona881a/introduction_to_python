from point import Point
from plane import Plane
from math import linear_function_find_slope

def sortCoordinates(p): 
    return p[1] - p[2]

list_of_points = [
    Point(1,5),
    Point(),
    Point(1),
    Point(20,-1),
    Point(10,15)
]

for point in list_of_points:
    print(point)

print("\nIs Point.getCoordinates() instance of tuple: {} ".format(isinstance(list_of_points[0].getCoordinates(),tuple)))
print("\nIs Point instance of tuple: {}".format(isinstance(list_of_points[1], tuple)))

p1 = Point(2,5)
p2 = Point(10,10)

linear_function_find_slope(list_of_points[0], list_of_points[4])
linear_function_find_slope(x1= p1.x, x2= p2.x, y1=p1.y, y2=p2.y)

#Sortering af coordinater fungere ikke med den almindelige sort function
list_of_points.sort()
print([point.getCoordinates() for point in list_of_points])
print("\n")

#print(dict(p1))

plane = Plane(x=10, y=10)
print(plane.x_boundary)
print(plane.y_boundary)

print(plane)

#Sorting a list of tuples
#sorted(list_of_points, key=sortCoordinates)

