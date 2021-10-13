"""
8. Concatenate two lists index-wise
"""

list1 = ['Hi ', 'Jahid ', 'Laboni ']
list2 = ['Mr', 'Hasan', 'Akter']

print("Given List1 :", list1)
print("Given List2 :", list2)

result = [i+j for i, j in zip(list1, list2)]
print("The list after element concatenation is : ", result)

