from random import randint


class Bank:

  def __init__(self):
    self.accounts = []
  
  def addAccounts(self, *accounts):
    print("line 10", accounts)

    for account in accounts:
      self.accounts.append(account)
  
  def deleteAccount(self, account):
    self.accounts.remove(account)

  def __str__(self):
    print()
    str = "The Banks current accounts:\n\n"

    for account in self.accounts:
      str += f'{account}\n'

    return str

class Account:

  def __init__(self,customer,balance = 0):
    self.customer = customer
    self.balance = balance
    self.bankNo = randint(1,9999999)

  def __str__(self):
    return f'Customer: {self.customer}, The Balance of the Customer: {self.balance}, Bank No. {self.bankNo}'

class Customer:

  def __init__(self,*args):
    if len(args) == 1:
      self.firstname = args[0]
    elif len(args) == 2:
      self.firstname = args[0]
      self.lastname = args[1]
    elif len(args) == 3:
      self.firstname = args[0]
      self.middlename = args[1]
      self.lastname = args[2]
    
  def __str__(self):
    str = f'Firstname: {self.firstname}'

    if len(self.__dict__) == 3:
      str += f' Middlename: {self.middlename} Lastname: {self.lastname}'
    elif len(self.__dict__) == 2:
      str += f' Lastname: {self.lastname}'
    
    return str

bank = Bank()
print(bank)

customer1 = Customer("Jonas","Kunert")
customer2 = Customer("Rasmus")
customer3 = Customer("Oliver","Skau")
customer4 = Customer("John","Didele","Doe")

#Verifying that the *args works
print(customer1.__dict__)
print(customer4.__dict__)


#Adding the accounts to the bank
bank.addAccounts(Account(customer1,4950),Account(customer2),Account(customer3, 1000000),Account(customer4,100))

print(bank)