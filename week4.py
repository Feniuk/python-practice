# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def report_pet(self):
#         print("Name: ", self.name, "/ Age: ", self.age)

# p1_obj = Pet("Misha", 12)
# p2_obj = Pet("Alex", 42)

# p1_obj.report_pet()
# p2_obj.report_pet()

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def greet_person(self):
#         print("Hello loved: ", self.name, "/ Your age is", self.age)

# person1_obj = Person("Misha", 88)
# person1_obj.greet_person()

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
    
#     def calculate_area(self):
#         area = self.width * self.height
#         print("Area =", area)

#     def calculate_perimeter(self):
#         perimeter = 2 * self.width + 2 * self.height
#         print("Perimeter =", perimeter)

# data_obj = Rectangle(3, 4)
# data_obj.calculate_area()
# data_obj.calculate_perimeter()

# class BankAccount:
#     def __init__(self, balance, ):
#         self.balance = float(balance)

#     def withdraw_money(self, amount):
#         if amount > self.balance:
#             print(f"You have low account balance {self.balance}")
#         else: 
#             self.balance -= amount
#             print(f"You have successfully withdrawn {amount}\nYour current balance is:", self.balance)

#     def deposit_money(self, amount):
#         self.balance += amount
#         print("You have successfully deposited", amount,"\nYour current balance is:", self.balance)

# balance_obj = BankAccount(1000)
# balance_obj.deposit_money(100)
# balance_obj.withdraw_money(100)

# class Car:
#     def __init__(self, mark, model, year):
#         self.mark = mark
#         self.model = model
#         self.year = year
    
#     def description(self):
#         print(f"Mark: {self.mark}\nModel: {self.model} \nYear:{self.year}")

# car_obj = Car("Lamborghini", "Urus Perfomante", 2025)
# car_obj.description()

def divide_by(num1, num2):
    return num1 / num2

num1 = 2
num2 = 8
try:
    divide_by(num1, num2)
except ZeroDivisionError:
    print("You have entered 0 ")