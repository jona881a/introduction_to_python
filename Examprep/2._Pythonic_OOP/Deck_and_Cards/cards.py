from card import Card

class Cards(object):

  def __init__(self):
    colors = ['heart', 'diamonds', 'spades', 'clubs']
    self.cards = [Card(value, color) for value in range(1, 14) for color in colors]


  def __add__(self, other):
    return self + other

  def __delitem__(self,key):
    return self.cards.pop(key)

  def __str__(self):
    return str([str(card) for card in self.cards])

  def __len__(self):
    return len(self.cards)
"""
  def __getitem__(self, key):
    return self.__cards[key]

  def __setitem__(self, key, other):
    self.cards[key] = other

"""