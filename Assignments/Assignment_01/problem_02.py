"""
 2.Given a range of the first 10 numbers, Iterate from the start number to the end number, and In each iteration
 print the sum of the current number and previous number

"""

previous_num = 0
for i in range(10):
    sum = previous_num + i
    print(f'Current number {i} Previous Number {previous_num} is {sum}')
    previous_num = i