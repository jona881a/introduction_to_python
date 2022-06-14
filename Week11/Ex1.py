def averager():
  total = 0.0
  count = 0
  avg = None
  while True:
    temp = yield avg
    total += temp
    count += 1
    avg = total / count

x = averager()
next(x)

for i in range(10):
  print(x.send(i))

