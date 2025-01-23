# int - числа (целые)
# str - текст
# float - числа (не целые)
# bool - true / false
from random import choice

# num1 = input("Insert numbers: ")
# num2 = input("Insert numbers: ")
# summa = num1 + num2
# minus = num1 - num2
# print(summa, minus)

# a = 5.45
# print(a)
# b = int(a)
# print(b)

# num1 = float(input("Insert:"))
# num2 = float(input("Insert: "))
# print(f"number 1 = {num1}, number 2 = {num2}, summa = {num1 + num2}")

bmw = 300000
hyundai = 120000
mercedes = 230000
tesla = 400000

budget = 500000

print(f"ur budget: {budget}.\n"
      f" If u buy BMW, u will have one: {budget - bmw}.\n"
      f" If u buy Hyundai, u will have one: {budget - hyundai}.\n"
      f" If u buy Mercedes, u will have one: {budget - mercedes}.\n"
      f" If u buy Tesla, u will have one: {budget - tesla}.\n"
      f"We have a promotion for your first purchase, 10% discount.\n"
      f"Discount for BMW: {bmw - 1}")

print("what is ur choice?")
myChoice = input("Insert ur choice: ")
print("My choice is:", myChoice)
