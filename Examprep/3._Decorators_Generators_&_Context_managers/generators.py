class PowTwo:
    def __init__(self, max=0):
        self.n = 0
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        result = 2 ** self.n
        self.n += 1
        return result

def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1

def AUTO_INCREMENT():
  num = 0
  while True:
    yield num
    num += 1

#Lav metoden om så den kan søge i en database eller csv fil?
def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
          return line