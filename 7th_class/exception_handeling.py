# print("Exception Handeling")

# try:
#     number = int(input())
#     print("num is:", 100/number)

# except ZeroDivisionError as e:
#     print("Do not use zero")

# print("Jahid")


""" multi exception / build in exception"""

def error_handeling():
    try:
        number = int(input())
        print("num is:", 100/number)

    except Exception as e:
        print(e)
        error_handeling()

error_handeling()




