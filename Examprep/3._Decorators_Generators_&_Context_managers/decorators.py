import functools
import time

def performance_timer(func):
  @functools.wraps(func) #Needed due to introspection, else the func doesn't know itself
  def wrapper_performance_timer(*args, **kwargs):
    start_time = time.perf_counter()
    value = func(*args,**kwargs)
    end_time = time.perf_counter()
    run_time = end_time - start_time
    wrapper_performance_timer.time_waited += run_time
    print("Finished {!r} in {:.4f} secs".format(func.__name__,run_time))
    print(f"Time waited total: {wrapper_performance_timer.time_waited:.4f} secs")
    return value
  wrapper_performance_timer.time_waited = 0
  return wrapper_performance_timer

def do_n_times(n):
  def decorator_do_n_times(func):
    @functools.wraps(func)
    def wrapper_do_n_times(*args, **kwargs):
      for i in range(n):
        print(f'Doing it {i} time')
        value = func(*args, **kwargs)
      return value
    return wrapper_do_n_times
  return decorator_do_n_times

def authentication_required(func):
  pass
