class Makeparagraph:
  def __init__(self, paragraph):
    self.paragraph = paragraph

  def __enter__(self):
    print('<p>')

  def __exit__(self, *args):
    print('</p>')