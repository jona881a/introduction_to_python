import csv

def create_datastructure_from_csv(path, type, listFor):
  datastructure = None

  if type.lower() == "set":
    datastructure = set()

  with open(path,'r') as file:
    csvreader = csv.reader(file)

    headers = next(csvreader) 
    index = headers.index(listFor)

    rows = [row for row in csvreader]

    for col in rows:
      datastructure.add(col[index])

  return datastructure

def find_occurences_of_attribute(path, attribute):
  with open(path,'r') as file:
    csvreader = csv.reader(file)

    headers = next(csvreader) 
    rows = [row for row in csvreader]
    cells = []

  for col in rows:
    cells.append(col[headers.index(attribute)])

  dict = {}

  for attr in cells:
    count = cells.count(attr)
    dict[attr] = count

  return dict

def max_occurence(dict):
  max = None

  for item in dict.items():
    if max is None:
      max = item
    elif max[1] < item[1]:
      max = item

  return max
    