class Point(object):

    def __init__(self, *coordinates):
        if len(coordinates) == 1 and coordinates[0]:
            self.x = coordinates[0]
            self.y = 0
        elif len(coordinates) == 2:
            self.x = coordinates[0]
            self.y = coordinates[1]
        else:
            self.x = 0
            self.y = 0
    
    def getCoordinates(self):
        return tuple((self.x, self.y))

    def __str__(self):
        return "x: {}, y: {}".format(self.x,self.y)