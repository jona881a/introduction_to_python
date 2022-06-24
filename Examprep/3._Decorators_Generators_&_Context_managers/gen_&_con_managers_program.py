from ast import Pow
from context_managers import *
from generators import *
from decorators import * 
from sqlite3 import connect

with connect('../testdata/testdatabase.db') as conn:
  create_statement = create_db_statemet_from_csv('../testdata/persondata.csv', 'persondata')
  insert_statement = create_insert_statement('../testdata/persondata.csv', 'persondata')
  cur = conn.cursor()
  cur.execute('DROP TABLE IF EXISTS persondata')
  cur.execute(create_statement)
  cur.execute(insert_statement)

  for i in cur.execute('SELECT * FROM persondata LIMIT 100'):
    print(i)

  cur.execute('DROP TABLE persondata')

#Lav en ny context manager med bildatabasen og lav en generator som tager dig igennem de enkelte rækker
#af biler og dermed kan man "browse" bil kataloget, her skal man kunne kategoriesere efter bilmærke osv

@performance_timer
def time_iteration(it):
  for i in it:
    print(i)

manual_it = iter(PowTwo(10))
for_it = iter(PowTwo(10000))
gen_exp = (x for x in PowTwo(10))

print("\nManual iteration")
print(next(manual_it))
print(next(manual_it))
print(next(manual_it))

print("\nFor loop")
print("\nTiming how long it takes to iterate and print over PowTwo(10000)")
#time_iteration(for_it)

print("\nList comprehension over generator expression")
print([x for x in gen_exp])

print("\nCan also be done with the next method")
gen_exp = (x for x in PowTwo(10))
print(next(gen_exp))

print("\nGenerator function: ")
for i in PowTwoGen(10):
  print(i)

print("\nAuto incrementing ids like in mysql")
ai = AUTO_INCREMENT()
print(next(ai))
print(next(ai))

print("\nA copy of the grep terminal command")

pattern = grep('hello')
next(pattern)

while True:
  searchstring = input("Write something here: ")
  match = pattern.send(searchstring)

  if match is not None:
    print("Found a match with: {}".format(searchstring))
    break


  

