#IF-ELSE CONDITION

value = int(input("Please Enter The Value:"))

# Intiger cobversion
# value = int(value)

if value <= 40: 
    print("He will buy it.")

else:
    print("He will not buy it.")



#Nested For condition

age = int (input("Enter your age :"))


if age >= 18:
    print("You can enter theater room. But you need id card for enter the room")
    id_card = input("Do you have Id card?")
    if id_card == "True":
        print("You have id. Now you can enter the theater room")
    else:
        print("You have no id card. You can't enter the theater room")
else:
     print("You are teenager you can't enter the room")       



#ladder
# ==, <=, >=, !=, or(|), and(&), not(!)

cgpa = int(input("Enter your cgpa: "))

if cgpa <= 5 & cgpa >= 4:
    print("Excelent")
elif cgpa <= 4 & cgpa >= 3:
    print("Avarage")
    
elif cgpa <=3 & cgpa >= 2:
    print("Good")
elif cgpa <= 2 & cgpa >= 1:
    print("Chap Nap diya pass")
else:
    print("Fail")

