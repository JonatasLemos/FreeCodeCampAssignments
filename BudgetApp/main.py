from spentChart import create_spent_chart
class Category:

    def __init__(self, name):
        self.name = name
        self.__ledger = []
        self.__balance = 0
        self.__lost_money = 0

    def deposit(self, amount, description=""):
        self.__append_ledger(amount,description)

    def withdraw(self, amount, description="",transfer=False):
        if self.__check_funds(amount):
            self.__append_ledger(-amount,description)
            if not transfer:
                self.__lost_money += amount
            return True
        return False

    def transfer(self, amount, category):
        if self.__check_funds(amount):
            category.deposit(amount, f"Transfer from {self.name}")
            self.withdraw(amount, f"Transfer to {category.name}",True)
            return True
        return False

    def __append_ledger(self, amount, description):
        self.__ledger.append({"amount": amount, "description": description})
        self.__balance += amount

    def __check_funds(self, amount):
        return amount < self.__balance

    @property
    def balance(self):
        return self.__balance

    @property
    def lost_money(self):
        return self.__lost_money

    def __str__(self):
        category_name = f"{self.name}".center(30, "*")
        values = ""
        for i in range(len(self.__ledger)):
            length = len(self.__ledger[i]["description"])
            description = self.__ledger[i]["description"]
            amount = format(float(self.__ledger[i]["amount"]), ".2f")
            length_amount = len(amount)
            trim = 30-(length_amount+1)
            if length > trim:
                description = self.__ledger[i]["description"][0:trim]+" "
            values += description + amount.rjust(30-length) + "\n"
        total = format(self.__balance, ".2f")
        text = category_name + "\n" + values + "Total: " + total
        return text

# Creating objects amd calling create_spend_chart function
food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")
food.deposit(1000, "initial deposit")
business.deposit(2560,"initial deposit")
business.withdraw(100,"equipments")
entertainment.deposit(900, "initial deposit")
food.withdraw(45.67, "milk, cereal, eggs")
food.transfer(20, entertainment)
entertainment.withdraw(45.67, "show")
entertainment.transfer(20, business)

# Printing ledger
print(food)

# Printing spend
print(create_spent_chart([business,entertainment,food]))
