# class : object blue print

class Teacher:
    # class => attribute and function
    # attribute => variable => 1. global variable 2. local variable

    # global variable

    name = ""
    id = ""


    # constractor => initalization global variable
    def __init__(self, name , id):
        self.name = name
        self.id = id

    #function
    def get_name(self):
        return self.name

    # local variable as a perameter
    def set_name(self , name):
        self.name = name


    # local variable in function
    def versity_name(self):
        #local variable
        versity = "DIU"
        return self.versity


# object
teacher = Teacher( "Tamim", "146-21-33")
print ("Name is:", teacher.name,", " "Id is:", teacher.id)

teacher2 = Teacher("Jahid" , "173-35-266")
print ("Name is:", teacher2.name,", " "Id is:", teacher2.id)


