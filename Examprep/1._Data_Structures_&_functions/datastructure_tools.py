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

#Skal laves generel til alle slags kolonner i csv filer
def find_same_names(list):
  namedict = {}

  for name in list:
    count = 0
    for othername in list:
      if name.lower() == othername.lower():
        count += 1
        namedict[repr(name)] = count

  return namedict
