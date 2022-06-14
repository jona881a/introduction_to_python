class OpenFile():
  def __init__(self, filename, mode):
    self.filename = filename
    self.mode = mode

  def __enter__(self):
    print('__enter__')
    self.file = open(self.filename, self.mode)
    return self.file

  def __exit__(self, *args):
    print('__exit__')
    self.file.close()