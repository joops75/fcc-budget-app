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
  # collect category info
  category_info = []
  withdrawals_tot = 0
  max_name_length = 0
  for category in categories:
    category_info.append([category.category])
    withdrawals = 0
    name_length = len(category.category)
    if name_length > max_name_length:
      max_name_length = name_length
    for transaction in category.ledger:
      amount = transaction["amount"]
      if amount < 0:
        withdrawals -= amount
        withdrawals_tot -= amount
    category_info[-1].append(withdrawals)

  # create output list
  output = ["Percentage spent by category"]

  # add lines to output list
  for i in reversed(range(0, 101, 10)):
    output.append("{:3d}| ".format(i))

    for info in category_info:
      output[-1] += "{}  ".format("o" if info[1] and (100 * info[1] / withdrawals_tot) >= i else " ")

  output.append("    -" + "-" * len(categories) * 3)

  for i in range(0, max_name_length):
    output.append(" " * 5)
    for j in range(0, len(categories)):
      try:
        output[-1] += categories[j].category[i] + " " * 2
      except:
        output[-1] += " " * 3

  # return new-line separated string from output list 
  return '\n'.join(output)