from decimal import Decimal

class Category:
  def __init__(self, category):
    self.category = category
    self.ledger = []

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})

      return True

    else:
      return False

  def get_balance(self):
    balance = 0
    
    for transaction in self.ledger:
      balance += transaction["amount"]

    return balance

  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + category.category)

      category.deposit(amount, "Transfer from " + self.category)

      return True

    else:
      return False

  def check_funds(self, amount):
    balance = self.get_balance()

    return balance >= amount

  def __str__(self):
    output = [self.category.center(30, "*")]

    for item in self.ledger:
      output.append(item["description"][:23].ljust(23, " ") + str(Decimal(item["amount"]).quantize(Decimal("1.00"))).rjust(7, " "))

    output.append("Total: " + str(Decimal(self.get_balance()).quantize(Decimal("1.00"))))

    return "\n".join(output)

def create_spend_chart(categories):
  pass