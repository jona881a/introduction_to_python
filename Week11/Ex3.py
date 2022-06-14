from sqlite3 import connect
from contextlib import contextmanager
"""
with connect('school.db') as conn:
  cur = conn.cursor()
  cur.execute('CREATE TABLE students(id int PRIMARY KEY, name text, cpr text)')
  cur.execute('INSERT INTO students(id, name, cpr) VALUES (1, "Claus", "223344-5566")')
  cur.execute('INSERT INTO students(id, name, cpr) VALUES (2, "Julie", "111111-1111")')
  cur.execute('INSERT INTO students(id, name, cpr) VALUES (3, "Hannah", "222222-2222")')

  for i in cur.execute('SELECT * FROM students'):
    print(i)

  cur.execute('DROP TABLE students')
"""

@contextmanager
def CREATE_TABLE(name, *args):
  statement = ''
  for arg in args:
    statement += arg
  return f'{name}( + statement)'