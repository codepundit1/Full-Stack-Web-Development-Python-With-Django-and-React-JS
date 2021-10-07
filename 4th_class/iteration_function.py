for i in range(7):
    print(i)

#iteration function
print(range(45)) #This is built in function and iterator function


#iterator vs generator
#Generation is custom function which we create
print('-'*80)

def my_range(endnum):
    for i in range(endnum):
        yield i

for i in my_range(20):
    print(i)

print("="*40)
# map(func,iter), reduce(func, seq), filter(func, seq)
#map

my_number = lambda x:x

print(list(map(my_number, [77, 55, 4])))

#reduce
import functools
list = [1, 3, 5, 6, 2, ]
 
# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a+b, list))

# filter function 
print("--filter--" * 10)

def even_number(number):
    if number % 2 == 0:
        return True
    return False

result = filter(even_number, [1, 3, 4, 7, 8, 10])
print(list(result))