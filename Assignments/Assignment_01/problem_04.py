"""
4. Accept number from user and calculate the sum of all number from 1 to a given number
"""


num = int(input("Enter number:"))
sum = 0
for i in range(1, num + 1, 1):
    sum = sum + i
print("Sum of all numbers is: ", sum)

