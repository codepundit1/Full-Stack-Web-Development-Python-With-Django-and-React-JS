
"""
5. Given a list, iterate it, and display numbers divisible by five, and if you find a number greater than 150, stop the loop iteration.
"""

numbers = [5, 20, 30, 50, 70, 80, 200, 300, 100]

for i in numbers:
    if i % 5 == 0:
        if i > 150:
            break
        else:
            print(i)
