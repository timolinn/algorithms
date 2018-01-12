'''
Created on Nov 29, 2016

@author: Timolinn
'''
class BankAccount:
  def deposit(self):
    pass

  def withdraw(self):
    pass

class SavingsAccount(BankAccount):
  def __init__(self, balance = 500):
    BankAccount.__init__(self)
    self.balance = balance #Minimum balance of the savings Account

  def deposit(self, amount):
    if amount < 0: #for negative amounts
      return "Invalid deposit amount"
    else:
      self.balance += amount
      return self.balance
  def withdraw(self, amount):
    if amount > self.balance:
      return "Cannot withdraw beyond the current account balance"
    elif self.balance - amount < 500:
      return "Cannot withdraw beyond the minimum account balance"
    elif amount < 0:
      return "invalid withdraw amount"
    else:
      self.balance -= amount
      return self.balance

class CurrentAccount(BankAccount):
  def __init__(self):
    BankAccount.__init__(self)
    self.balance = 0
  def deposit(self, amount):
    if amount < 0: #for negative amounts
      return "Invalid deposit amount"
    else:
      self.balance += amount
      return self.balance

  def withdraw(self, amount):
    if amount > self.balance:
      return "Cannot withdraw beyond the current account balance"
    elif amount < 0:
      return "invalid withdraw amount"
    else:
      self.balance -= amount
      return self.balance

class Account(object):
    counter = 0
    def __init__(self, holder, number, balance,credit_line=1500):#Class constructor
        Account.counter += 1
        self.__Holder = holder
        self.__Number = number
        self.__Balance = balance
        self.__CreditLine = credit_line


    def __del__(self):#Class destructor
        Account.counter =  1

def main():
    tim = SavingsAccount()
    print(tim.deposit(5000))
    print(tim.withdraw(5000))


if __name__=="__main__": main()