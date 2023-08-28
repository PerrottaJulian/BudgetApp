class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []
    self.spent = 0
    
  def deposit (self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw (self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": amount*-1, "description": description})
      self.spent += amount
      return True
    else:
      return False
      
  def get_balance(self):
    balance = 0
    for i in self.ledger:
       balance += i["amount"]
    return balance

  def transfer(self, amount, category):
    if self.withdraw(amount, f"Transfer to {category.name}") is False:
      return False
    else:
      category.deposit(amount, f"Transfer from {self.name}")
      return True

  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    else:
      return True
  def __repr__(self):
    lenght = 30
    dots_line = "*"*int((lenght - len(self.name)) / 2)
    final_string = dots_line+self.name+dots_line+"\n"
    for i in self.ledger:
      des = i["description"][0:23]
      am = format(float(i["amount"]), ".2f")
      line = des + str(am).rjust(30-len(des))+"\n"
      final_string += line
    final_string += "Total: "+ str(self.get_balance())
    return final_string



def create_spend_chart(categories):
  total_spent = 0 
  chart = "Percentage spent by category\n"

  names = []
  
  namescolumn = ""
  #percentaje
  for category in categories:
    total_spent += category.spent
    names.append(category.name)
  percentages_cateogries = {}
  for category in categories:
    percentage = category.spent*100/total_spent
    rounded_percentage = round(percentage/10)*10
    if rounded_percentage == 10:
      rounded_percentage = 0 #shouldnt be necesary
    percentages_cateogries[category.name] = rounded_percentage

  #numbers and dots
  numbers = 110
  for i in range (11):
    numbers -=10
    chart += (str(numbers) + "| ").rjust(5) 
    for category in categories:
      if percentages_cateogries[category.name] >= numbers:
        chart += "o  "
      else:
        chart += "   "
    chart += "\n"
  

  #vertical names
  for i in range(len(max(names, key=len))):
    namescolumn += "\n" 
    namescolumn += "     "
    for category in categories:
      try:
        namescolumn += category.name[i] + "  "
      except:
        namescolumn += "   "
  
    
  chart += "    " + "-" + "-"*3*len(categories)
  chart  += namescolumn
      
    
  return chart
