students = {
    "1234":{
        "name" : " Jahid Hasan Shiplo",
        "dept" : "CSE"
    },

    "5678":{
        "name" : " Jahid Hasan",
        "dept" : "eee"
    },
    
    "9101":{
        "name" : "Shiplo",
        "dept" : "swe"
    },

}

def find_student(id):
    student_info = students.get(id)
    if student_info == None:
        print("No student info found")
    else:
        print('Name:',student_info["name"],'And Dept:', student_info["dept"])
        
find_student("5678")

#Arguments
def get_num(*num, **kwargs):
    print(num)
    print(kwargs)

get_num(4, 5, 5, 63, 54, 44, 87, name = "Shiplo", Dept = "SWE")


# return and print matter
def mix_arg(name, age, *args, **kwargs):
    return name + " " + str(age)

print(mix_arg("shiplo", 90))

