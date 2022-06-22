from context_managers import *
from sqlite3 import connect

create_statement = create_db_statemet_from_csv('../testdata/persondata.csv', 'persondata')
insert_statement = create_insert_statement('../testdata/persondata.csv', 'persondata')

with connect('../testdata/testdatabase.db') as conn:
  cur = conn.cursor()
  cur.execute('DROP TABLE IF EXISTS persondata')
  cur.execute(create_statement)
  cur.execute(insert_statement)


  for i in cur.execute('SELECT * FROM persondata LIMIT 100'):
    print(i)

  cur.execute('DROP TABLE persondata')
