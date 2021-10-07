"""
01. Given two integer numbers return their product. 
If the product is greater than 1000, then return their sum.
"""
num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))

product = num1 * num2

if product > 1000:
    sum = num1 + num2
    print(sum)
else:
    print(product)