import functools
from multiprocessing.connection import wait
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
      for _ in range(n):
        value = func(*args, **kwargs)
      return value
    return wrapper_do_n_times
  return decorator_do_n_times

def authentication_required(func):
  pass

def count_time_waited(func):
  @functools.wraps(func)
  def wrapper_count_calls(*args, **kwargs):
    wrapper_count_calls.num_calls += 1
    print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
    return func(*args, **kwargs)
  wrapper_count_calls.num_calls = 0
  return wrapper_count_calls