def api():
  yield 'do_this_first'
  yield 'do_this_second'
  yield 'do_this_third'

def simple_coroutine():
  print('-> coroutine started')
  x = yield
  print(f'-> coroutine recieved: {x}')

api = api()

print(next(api))
print(next(api))
print(next(api))

x = simple_coroutine()
print(x)
x.send(1)
print(next(x))
