from decorators import *
import csv, ast

def find_data_type(value, current_type):
  try:
    type = ast.literal_eval(value)
  except ValueError:
    return 'varchar'
  except SyntaxError:
    return 'varchar'

  if type(type) in [int, float]:
    if (type(type) in [int, float] and current_type not in ['float','varchar']):
      return 'int'
    if type(type) is float and current_type not in ['varchar']:
      return 'decimal'
  else:
    return 'varchar'

@performance_timer
def create_db_statemet_from_csv(path, tablename):
  longest = []
  headers = []
  type_list = []

  with open(path, 'r')  as file:
    csvreader = csv.reader(file)
    for row in csvreader:
      if len(headers) == 0:
        headers = row
        for col in row:
          longest.append(100)
          type_list.append('')

      else:
        for i in range(len(row)):
            if type_list[i] == 'varchar' or row[i] == 'NA':
                pass
            else:
                type_list[i]  = find_data_type(row[i], type_list[i])

  statement = f'CREATE TABLE {tablename} (id INTEGER PRIMARY KEY AUTOINCREMENT, '

  for i in range(len(headers)):
    if type_list[i] == 'varchar':
        statement = (statement + '\n{} varchar({}),').format(headers[i].lower(), str(longest[i]))
    else:
        statement = (statement + '\n' + '{} {}' + ',').format(headers[i].lower(), type_list[i])

  return statement[:-1] + ');'


@performance_timer
def create_insert_statement(path, tablename):

  with open(path,'r') as file:
    csvreader = csv.reader(file)
    headers = next(csvreader)
    columns = ''
    
    for header in headers:
      columns += f'{header},'
    
    statement = f'INSERT INTO {tablename}({columns[:-1]}) VALUES'

    for row in csvreader:
      statement += '('

      for col in row:
        statement += "'{}',".format(col)
        
      statement = statement[:-1] + '),'

  return statement[:-1] + ';'
