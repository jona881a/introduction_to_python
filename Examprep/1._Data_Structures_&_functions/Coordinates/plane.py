from point import Point

class Plane(object):
  
  def __init__(self, *initial_coordinates, **dimensions):
      if len(dimensions) is not 0:
        self.xy_plane = [[Point(0,0)] * dimensions["x"]] * dimensions["y"]

        self.x_boundary = dimensions["x"]
        self.y_boundary = dimensions["y"]

      else:
        raise TypeError("Could not make plane with no dimensions specified")
  
  @property
  def get_x_boundary(self):
    return self.__x_boundary

  @property
  def get_y_boundary(self):
    return self.__y_boundary

  @property
  def get_xy_plane(self):
    return self.__xy_plane

  def __str__(self):
    return str(self.xy_plane)
    #for i in self.x_boundary:
      #for j in self.y_boundary:
        #print(self.xy_plane[i][j])

 # def __add__(self, point, **points):

 # def __contains__(point, **points):
    