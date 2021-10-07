d = {}
# key value pair -> key:value

d = {"key1": "value1", 2:30, 3:10.50}
print(d)
print(d["key1"])


for i, j in d.items():
    print(i, j)

print(d.get('key1'))


#nested item 

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

# print(students.get("1234"))

# students_info = students.get(input())

# if students_info == None:
#     print("No data")
# else:
#     print(students_info['name'], students_info['dept'])

print(d.keys())
print(d.values())


# d2 = { "key2", "value2"}

# d.update(d2)
# print(d)