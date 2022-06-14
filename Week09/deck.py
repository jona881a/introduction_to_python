class Deck:
  def __init__(self):
    self.cards = ['A','K',4,7]

  def __add__(self, other):
    return self + other

  def __len__(self):
    return len(self.cards)

  def __getitem__(self, key):
    return self.__cards[key]

  def __setitem__(self, key, other):
    self.cards[key] = other

  def __delitem__(self,key):
    del(self.cards[key])

  def __repr__(self):
    return f'{self.__dict__}'
