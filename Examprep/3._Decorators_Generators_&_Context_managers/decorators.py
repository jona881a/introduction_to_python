import functools
import time

def performance_timer(func):
  @functools.wraps(func) #Needed due to introspection, else the func doesn't know itself
  def wrapper_performance_timer(*args, **kwargs):
    start_time = time.perf_counter()
    value = func(*args,**kwargs)
    end_time = time.perf_counter()
    run_time = end_time - start_time
    print("Finished {!r} in {:.4f} secs".format(func.__name__,run_time))
    return value
  return wrapper_performance_timer
