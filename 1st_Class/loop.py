#  for loop & while loop
#for loop
for i in range(0, 20):
    if i % 2 == 0:
        print(i,"= is a even number")
    else:
        print(i,"= is a odd number")
# # while condition
i=0
n=10

while i<=n:
    print(i)
    i = i+2

count = 0
for i in ['one', 'two', 'two', 'two', 'three']:
    if i == 'two':
        print(i,"is found")
        count = count + 1
else:
    print("not found")

print(count)