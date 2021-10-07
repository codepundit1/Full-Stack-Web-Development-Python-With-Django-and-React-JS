def first_function():
    def second_function():
        print("inner function")
    second_function()
    print("outter function")


def outter_func(name):
    def inner_func():
        print("Welcome", name)
    return inner_func()

   
def fatctorial(number):
    try:
        if not isinstance(number, int):
            raise TypeError("Sorry, Number have to be intiger")
        if number < 0:
            raise ValueError("Numeber must be bigger than 0")
        
        
        def fact_cal(num):
            if num <=1 :
                return 1
            else:
                return num * fact_cal(num -1)

        return fact_cal(number)
    except Exception as e:
        print (e)


#Lambda function
# def num(x):
#     if x == 10:
#         return x**3
#     else:
#         return x

num = lambda x:x**3 if x == 10 else x
print(num(110))
print("_"*10)

print(fatctorial(-4))

first_function()
outter_func("Jahid")


#another lambda

another_lambda = lambda a, b: a+b if a==10 and b==20 else a*b
print(another_lambda(20 , 4))
