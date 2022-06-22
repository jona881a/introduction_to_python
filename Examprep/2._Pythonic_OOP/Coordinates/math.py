def linear_function_find_slope(*points, **coordinates):
  values = []

  if len(points) is not 0:
    values = points
  elif len(coordinates) is not 0:
    print(coordinates)
    values = coordinates.values()
  else:
    raise TypeError("No values specified, calculation could not be performed")
