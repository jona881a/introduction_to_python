class Point(object):

    def __init__(self, *coordinates):
        if len(coordinates) == 1:
            self.x = coordinates[0]
        elif len(coordinates) == 2:
            self.x = coordinates[0]
            self.y = coordinates[1]
    
    def getCoordinates(self):
        if self.x == None:
            return (self.x)
        elif self.y == None:
            return (self.y)
        elif self.y == None and self.x == None:
            return "no coordinates found"
        else:
            return tuple((self.x, self.y))