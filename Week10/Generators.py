from time import sleep

class Compute:
  def __call__(self):
    l = []
    for i in range(10):
      sleep(.5)
      l.append(i)
      print(l)
    return l

  def __iter__(self):
    self.last = 0
    return self

  def __next__(self):
    if self.last > 9:
      raise StopIteration()
    temp = self.last
    self.last += 1

    sleep(.5)

    return temp

 
c = Compute()
#c()
"""
it = iter(c)
for i in it:
  print(i)

#print(callable(c))

"""

def gen_comp():
  for i in range(10):
    yield i

it = gen_comp()

print(next(it))

list_comprehension = [ i if i % 2 == 0 else 'Booo' for i in range(10)]
gen_expr = (i if i % 2 == 0 else 'Booo' for i in range(10))

print(list_comprehension)

it = iter(gen_expr)

for i in it:
  print(i)
