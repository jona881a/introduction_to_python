class Person:
  def __init__(self, *args):
    if len(args) == 1:
      self.name = args[0] #Instance variable
    elif len(args) == 2:
      self.name = args[0]
      self.age = args[1]

  def birthday(self, age):
    self.age = age
    return f'Happy birthday! {self.name}, you are now 1 year older which means you are {self.age} old now!'
  
  def __str__(self):
    return f'Hello! My name is {self.name} and im {self.age} old'


p = Person("Jonas",23)

print(p)
print (p.birthday(24))