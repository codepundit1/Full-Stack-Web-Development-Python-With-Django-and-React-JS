#data structure == collections
# 1. list 2. tuple 3. set 4. dictionary

l = [1, 2, 5, 6, 8, 3]
print(type(l))
print(l)

# for i in l:
#     print(i)
#     print(type(i))

#indexing
print(l[4])

#slicing
print(l[2:6])
print(l[-1])

#revers order
print(l[::-1])

#list mutable collection
l[0] = 100
print(l)

l = l+[1000]
print(l)

#build in function

l.append(500)
print(l)

l.reverse()
print(l)

l.sort()
print(l)

l.pop(5)
print(l)

print(l.count(500))

#comprehension
l1 = [i for i in range(10)]
print(l1)