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

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y

    def getCoordinates(self):
        return tuple((self.__x, self.__y))

    def __dict__(self):
        return self.__dict__

    def __str__(self):
        return "x: {}, y: {}".format(self.x,self.y)