from point import Point

def sortCoordinates(): 
    pass

list_of_points = [
    Point(1,5),
    Point(),
    Point(1),
    Point(20,-1),
    Point(10,15),
]

for point in list_of_points:
    print(point)

print("Is Point.getCoordinates() instance of tuple: {} ".format(isinstance(list_of_points[0].getCoordinates(),tuple)))

#Sorting a list of tuples
sorted(list_of_points, key=sortCoordinates)


