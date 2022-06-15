class Player(object):

  def __init__(self, name):
    self.name = name

  @property
  def name(self):
    return self.__name

  @name.setters
  def name(self, newName):
    if type(newName) == str:
      self.__name = newName
    else:
      print("Wrong type of {}".format(type(newName)))
